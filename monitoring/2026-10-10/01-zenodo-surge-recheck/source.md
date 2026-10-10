# Source

- Probe: local stdlib Python collector (`zenodo_monitor_capture.py`), one GET per
  concept recid against `https://zenodo.org/api/records/<concept-recid>`, 3-attempt
  retry, 0.8 s spacing, raw responses retained per object
- Canonical recid table: `tools/check.py` -> `check_canonical_object_mapping`
- Capture window: 2026-10-10T13:12:08+00:00 to 2026-10-10T13:23:06+00:00 (UTC), 11/11 requests HTTP 200
- Intraday context captures earlier on 2026-10-10 (06:01, 07:34-07:45, 12:26 UTC)
  were taken with a four-metric probe and a mixed recid table; canonical values
  in this record supersede those readings
- A user-supplied independent cloud capture (15:0x CST) provided unique-view
  values for cross-verification; per-object agreement on eight of ten fixed
  objects, remainder explained by pipeline batch lag
- An external agent-generated audit timeline (12 observation segments,
  10-01 to 10-10) was used as narrative context only; its segment data originate
  from that agent's own earlier-built monitoring mechanism and are cited, not
  adopted, into this ledger
- Counting rules: `schema/counting-rules.md`; fixed ten kept separate from the
  audit runtime; no imputation; failed requests remain request outcomes
