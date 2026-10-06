#!/usr/bin/env python3
"""ZQB - Zenodo Query Conformance benchmark (exploratory tool, not a preregistered analysis).

Probes the *query layer* of the same open scholarly infrastructure the preregistered
study observes. Eleven conformance tests encode observed API contracts as invariants
(structure, key location, relation, HTTP semantics); none depend on rolling counters.

Scope discipline (mirrors analysis/README.md):
- This is an exploratory tool. It is not a preregistered primary analysis, does not
  touch the RS01-RS10 fixed corpus values, the six infrastructure layers, the 60
  object-layer units, or any prospective observation rule.
- Allowed channels only: zenodo.org/api, api.datacite.org, doi.org/api.
- Rate discipline: >=7s between Zenodo requests (observed WAF cooldown after 20+
  rapid requests), >=1s otherwise. A 403 "unusual traffic" response is a cooldown
  penalty, not a ban: mark-and-skip, never hammer.

Scoring: 10 points per test = path selection (5) + invariant verification (5).
Traps are documented per test; hitting a trap path scores 0 for that component.
Total 110, report also as percent.

Source: eleven field-recorded failure modes from the observation log
(2026-09-26 .. 2026-10-06), including: stats key location, Event Data list key,
hyphenated attribute keys, concept-redirect borrowing, versions endpoint absence,
quoted-search semantics, dual-handle retrieval split, embedded SWH tuple, three-tier
byline resolution, two distinct 404 semantics.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

ZENODO = "https://zenodo.org/api"
DATACITE = "https://api.datacite.org"
DOIORG = "https://doi.org/api"

# Fixed corpus anchors (concept/baseline/close per preregistration fixed corpus RS01).
WELCOME_CONCEPT = 22790907
WELCOME_BASELINE = 22790908
WELCOME_CLOSE_DOI = "10.5281/zenodo.23068145"
OSF_DOI = "10.17605/OSF.IO/5B329"
RC11_CONCEPT = 23166490
RC11_BETA = 23166491
HANDLE_DOI = WELCOME_CLOSE_DOI

UA = "zqb-query-conformance/1.0 (research-software-identity-audit; exploratory tool)"


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_NO_REDIRECT_OPENER = urllib.request.build_opener(_NoRedirect)


def fetch(url: str, timeout: int = 30, follow: bool = True):
    """Return (http_code, parsed_json_or_None, raw_head+final_url). One shot, no
    retries: conformance tests must observe the channel as-is. follow=False observes
    the raw redirect (urllib auto-follows by default - an observed trap: the same
    request reports 302 or 200 depending on client redirect policy)."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        opener = urllib.request.build_opener() if follow else _NO_REDIRECT_OPENER
        with opener.open(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", "replace")
            code = resp.status
            final = resp.geturl()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        code = exc.code
        final = exc.headers.get("Location") or exc.geturl() if exc.headers else exc.geturl()
    except Exception as exc:  # noqa: BLE001 - report transport failures verbatim
        return 0, None, f"transport: {exc}"
    head = f"final={final} || " + body[:160]
    try:
        return code, json.loads(body), head
    except json.JSONDecodeError:
        return code, None, head


class Report:
    def __init__(self) -> None:
        self.rows = []

    def add(self, test_id: str, name: str, path_ok: bool, invariant_ok: bool, note: str):
        score = (5 if path_ok else 0) + (5 if invariant_ok else 0)
        self.rows.append((test_id, name, path_ok, invariant_ok, score, note))

    def total(self) -> int:
        return sum(r[4] for r in self.rows)

    def render(self) -> str:
        out = ["ZQB conformance run", f"ts: {datetime.now(timezone.utc).isoformat(timespec='seconds')}"]
        for tid, name, p, i, s, note in self.rows:
            out.append(f"  {tid} {name:<34} path={'Y' if p else 'N'} invariant={'Y' if i else 'N'} score={s:>2} | {note}")
        out.append(f"TOTAL {self.total()}/110 ({100.0 * self.total() / 110:.1f}%)")
        return "\n".join(out)


def t01_metadata_location(rep: Report):
    """T1 title lives at metadata.title (top-level `title` is a duplicate, metadata is canonical)."""
    code, data, head = fetch(f"{ZENODO}/records/{WELCOME_BASELINE}")
    ok_path = code == 200 and isinstance(data, dict) and "metadata" in data
    inv = False
    note = ""
    if ok_path:
        md = data.get("metadata") or {}
        title = md.get("title")
        inv = isinstance(title, str) and len(title) > 0 and title == data.get("title")
        note = f"title={title!r}" if inv else f"metadata.title={title!r} top={data.get('title')!r}"
    else:
        note = f"http={code} {head}"
    rep.add("T01", "metadata location", ok_path, inv, note)


def t02_stats_location(rep: Report):
    """T2 stats block is top-level (not inside metadata); views >= unique_views invariant."""
    code, data, head = fetch(f"{ZENODO}/records/{WELCOME_BASELINE}")
    ok_path = code == 200 and isinstance(data, dict) and "stats" in data and "stats" not in (data.get("metadata") or {})
    inv = False
    note = ""
    if ok_path:
        s = data.get("stats") or {}
        keys = {"views", "unique_views", "downloads", "unique_downloads"}
        inv = keys <= set(s) and s.get("views", 0) >= s.get("unique_views", 0)
        note = f"views={s.get('views')} uv={s.get('unique_views')}"
    else:
        note = f"http={code} {head} (trap: reading metadata.stats)"
    rep.add("T02", "stats key location", ok_path, inv, note)


def t03_family_aggregation(rep: Report):
    """T3 dual stats plane: top-level four fields are family-level (identical across
    versions); version_* four fields are per-version (differ). Reading only one plane
    is a partial read of the same response."""
    code1, d1, h1 = fetch(f"{ZENODO}/records/{WELCOME_BASELINE}")
    time.sleep(7)
    code2, d2, h2 = fetch(f"{ZENODO}/records/23068145")
    ok_path = code1 == 200 and code2 == 200 and isinstance(d1, dict) and isinstance(d2, dict)
    inv = False
    note = ""
    if ok_path:
        s1, s2 = d1.get("stats") or {}, d2.get("stats") or {}
        fam = {"views", "unique_views", "downloads", "unique_downloads"}
        fam_same = all(s1.get(k) == s2.get(k) for k in fam)
        ver_differ = s1.get("version_views") is not None and s2.get("version_views") is not None \
                     and s1.get("version_views") != s2.get("version_views")
        inv = fam_same and ver_differ
        note = f"family same={fam_same}; version_views {s1.get('version_views')} vs {s2.get('version_views')}"
    else:
        note = f"http={code1}/{code2}"
    rep.add("T03", "family-level stats", ok_path, inv, note)


def t04_concept_anchor(rep: Report):
    """T4 conceptrecid == concept DOI tail; conceptdoi = 10.5281/zenodo.{conceptrecid}."""
    code, data, head = fetch(f"{ZENODO}/records/{WELCOME_BASELINE}")
    ok_path = code == 200 and isinstance(data, dict) and "conceptrecid" in data
    inv = False
    note = ""
    if ok_path:
        cr, cd = data.get("conceptrecid"), data.get("conceptdoi") or ""
        inv = str(cr) == cd.rsplit(".", 1)[-1] and cd.startswith("10.5281/zenodo.")
        note = f"conceptrecid={cr} conceptdoi={cd}"
    else:
        note = f"http={code} {head}"
    rep.add("T04", "concept anchor", ok_path, inv, note)


def t05_http_trichotomy(rep: Report):
    """T5 three HTTP semantics: 200 exists / 404 'persistent identifier does not exist' /
    302 concept borrowing (single-version family concept resolves to latest version)."""
    code_ok, d_ok, _ = fetch(f"{ZENODO}/records/{WELCOME_BASELINE}")
    time.sleep(7)
    code_404, d_404, _ = fetch(f"{ZENODO}/records/99999999")
    time.sleep(7)
    code_302, _, head_302 = fetch(f"{ZENODO}/records/{RC11_CONCEPT}", follow=False)
    ok_path = code_ok == 200 and code_404 == 404 and code_302 == 302
    inv = False
    note = ""
    if ok_path:
        msg404 = str(d_404.get("message") or "") if isinstance(d_404, dict) else ""
        # concept must redirect to a /api/records/{id} target different from the concept id
        # itself (latest-version borrowing). Target id is dynamic: new versions move it.
        import re as _re
        m = _re.search(r"final=/api/records/(\d+)", head_302)
        target = int(m.group(1)) if m else None
        inv = "persistent identifier" in msg404.lower() and target is not None and target != RC11_CONCEPT
        note = f"200/404/302 ok; 302->latest={target}"
    else:
        note = f"http={code_ok}/{code_404}/{code_302} (trap: urllib auto-follow turns 302 into 200)"
    rep.add("T05", "HTTP trichotomy", ok_path, inv, note)


def t06_versions_endpoint_trap(rep: Report):
    """T6 /records/{id}/versions does not exist (404 'Not found.'); distinct from T5 PID 404.
    Version chains are reached via conceptrecid/302, not a versions subresource."""
    code, data, head = fetch(f"{ZENODO}/records/{WELCOME_CONCEPT}/versions")
    ok_path = code == 404 and isinstance(data, dict)
    inv = False
    note = ""
    if ok_path:
        inv = (data.get("message") == "Not found.")
        note = f"versions endpoint 404 msg={data.get('message')!r} (distinct from PID 404)"
    else:
        note = f"http={code} {head} (trap: assuming /versions exists)"
    rep.add("T06", "versions endpoint absence", ok_path, inv, note)


def t07_dual_handle_retrieval(rep: Report):
    """T7 creator-handle vs title-handle retrieval split:
    q=lightlost (corpus creator) hits the ten-corpus families; q=lostlight530 hits
    only the instrument repo title. Bare and quoted forms agree on these tokens."""
    code1, d1, _ = fetch(f"{ZENODO}/records?q=lightlost&size=1")
    time.sleep(7)
    code2, d2, _ = fetch(f"{ZENODO}/records?q=lostlight530&size=1")
    ok_path = code1 == 200 and code2 == 200 and isinstance(d1, dict) and isinstance(d2, dict)
    inv = False
    note = ""
    if ok_path:
        t1 = ((d1.get("hits") or {}).get("total")) or 0
        t2 = ((d2.get("hits") or {}).get("total")) or 0
        # Mutual exclusion is the invariant: the corpus creator handle retrieves the
        # ten-family corpus; the instrument handle never retrieves corpus families.
        # The instrument-side count may be 0..1 (search index reindexes when a new
        # version is minted - observed 1 -> 0 transient on 2026-10-06).
        inv = t1 >= 10 and t2 <= 1
        note = f"lightlost={t1} (corpus) vs lostlight530={t2} (instrument; index transient allowed)"
    else:
        note = f"http={code1}/{code2}"
    rep.add("T07", "dual-handle retrieval split", ok_path, inv, note)


def t08_eventdata_double_trap(rep: Report):
    """T8 Event Data events live under top-level `data` (not `events`); attributes use
    hyphenated keys (relation-type-id); underscored keys silently return None."""
    code, data, head = fetch(f"{DATACITE}/events?doi=10.5281/zenodo.{WELCOME_CONCEPT}")
    ok_path = code == 200 and isinstance(data, dict) and isinstance(data.get("data"), list)
    inv = False
    note = ""
    if ok_path:
        evs = data.get("data") or []
        trap = data.get("events")
        if evs:
            attrs = evs[0].get("attributes") or {}
            inv = len(evs) >= 1 and attrs.get("relation-type-id") is not None and trap is None
            note = f"events_in_data={len(evs)} rt={attrs.get('relation-type-id')} events_key_trap={'present' if trap else 'absent'}"
        else:
            note = "data=[] (index lag)"
    else:
        note = f"http={code} {head} (trap: reading events key)"
    rep.add("T08", "EventData double trap", ok_path, inv, note)


def t09_handle_resolve(rep: Report):
    """T9 doi.org handle API resolves with responseCode 1; values[0].type is HS_ADMIN
    (the URL record lives in subsequent values, not values[0])."""
    code, data, head = fetch(f"{DOIORG}/handles/{HANDLE_DOI}")
    ok_path = code == 200 and isinstance(data, dict)
    inv = False
    note = ""
    if ok_path:
        vals = data.get("values") or []
        inv = data.get("responseCode") == 1 and bool(vals) and vals[0].get("type") == "HS_ADMIN"
        note = f"responseCode={data.get('responseCode')} values={len(vals)} first_type={vals[0].get('type') if vals else None}"
    else:
        note = f"http={code} {head}"
    rep.add("T09", "handle resolve", ok_path, inv, note)


def t10_embedded_swh(rep: Report):
    """T10 Zenodo record embeds the SWH tuple (swhid/origin/visit/anchor) - the archive
    face is observable from the record API without querying SWH endpoints."""
    code, data, head = fetch(f"{ZENODO}/records/{WELCOME_BASELINE}")
    ok_path = code == 200 and isinstance(data, dict) and "swh" in data
    inv = False
    note = ""
    if ok_path:
        swh = data.get("swh") or {}
        # The tuple lives inside one swhid string as semicolon parameters:
        # swh:1:dir:{hash};origin=https://doi.org/{doi};visit=swh:1:snp:{hash};anchor=swh:1:rel:{hash};path=...
        swhid = str((swh.get("swhid") or ""))
        inv = (
            swhid.startswith("swh:1:dir:")
            and ";origin=https://doi.org/" in swhid
            and ";visit=swh:1:snp:" in swhid
            and ";anchor=swh:1:rel:" in swhid
        )
        note = f"swhid={swhid.split(';')[0][:26]} origin_param={';origin=' in swhid} visit_param={';visit=swh:1:snp:' in swhid} anchor_param={';anchor=swh:1:rel:' in swhid}"
    else:
        note = f"http={code} {head} (trap: assuming SWH requires its own endpoint)"
    rep.add("T10", "embedded SWH tuple", ok_path, inv, note)


def t11_byline_tiers(rep: Report):
    """T11 three-tier byline resolution on one person:
    corpus creators = lightlost + ORCID id; instrument repo creator = lostlight530;
    OSF registration creator = real name with ORCID nameIdentifier. Verify all three
    layers resolve to their designated byline tier on the designated platforms."""
    code1, d1, _ = fetch(f"{ZENODO}/records/{WELCOME_BASELINE}")
    time.sleep(7)
    code2, d2, _ = fetch(f"{ZENODO}/records/{RC11_BETA}")
    time.sleep(7)
    code3, d3, _ = fetch(f"{DATACITE}/dois/{OSF_DOI}")
    ok_path = code1 == 200 and code2 == 200 and code3 == 200
    inv = False
    note = ""
    if ok_path:
        c_corpus = ((d1.get("metadata") or {}).get("creators") or [{}])[0].get("name")
        c_instr = ((d2.get("metadata") or {}).get("creators") or [{}])[0].get("name")
        dc_attrs = ((d3.get("data") or {}).get("attributes") or {})
        c_osf = (dc_attrs.get("creators") or [{}])[0].get("name")
        orcid_ids = [n.get("nameIdentifier") for n in (dc_attrs.get("creators") or [{}])[0].get("nameIdentifiers", []) if isinstance(n, dict)]
        inv = (
            c_corpus == "lightlost"
            and c_instr == "lostlight530"
            and c_osf == "Xuanyi Jiang"
            and any(isinstance(o, str) and o.endswith("0009-0001-3617-0832") for o in orcid_ids)
        )
        note = f"tiers: {c_corpus} / {c_instr} / {c_osf}+ORCID"
    else:
        note = f"http={code1}/{code2}/{code3}"
    rep.add("T11", "byline tier resolution", ok_path, inv, note)


TESTS = [t01_metadata_location, t02_stats_location, t03_family_aggregation, t04_concept_anchor,
         t05_http_trichotomy, t06_versions_endpoint_trap, t07_dual_handle_retrieval,
         t08_eventdata_double_trap, t09_handle_resolve, t10_embedded_swh, t11_byline_tiers]


def main() -> int:
    ap = argparse.ArgumentParser(description="ZQB Zenodo query conformance (exploratory tool)")
    ap.add_argument("--only", default="", help="comma list of T ids to run, e.g. T01,T08")
    args = ap.parse_args()
    only = {x.strip().upper() for x in args.only.split(",") if x.strip()}

    rep = Report()
    for fn in TESTS:
        tid = fn.__name__.split("_")[0].upper()
        if only and tid not in only:
            continue
        fn(rep)
        time.sleep(1)
    print(rep.render())
    return 0 if rep.total() >= 110 * 0.9 else 1


if __name__ == "__main__":
    sys.exit(main())
