"""Bounded public HTTP transport helpers for *future* diagnostics only.

Never reclassify a blocked/partial request as object absence. Historical
2026-11-13/15/17 collectors and their source ledgers remain immutable.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import BinaryIO

DEFAULT_BODY_LIMIT = 2_000_000
EDAM_OWL_BODY_LIMIT = 4 * 1024 * 1024


def response_limit(scope: str, key: str) -> int:
    """The EDAM ontology is ~3.4 MB; other requests retain the 2 MB guard."""
    return EDAM_OWL_BODY_LIMIT if (scope, key) == ("surface", "15:EDAM") else DEFAULT_BODY_LIMIT


def read_bounded(stream: BinaryIO, scope: str, key: str) -> tuple[bytes, str | None, int]:
    """Read one byte beyond the cap to distinguish a complete response from a prefix.

    On overflow, the returned prefix is diagnostic evidence, not a complete
    representation; do not attempt JSON parsing or claim identity verification.
    """
    limit = response_limit(scope, key)
    raw = stream.read(limit + 1)
    return raw, ("TRUNCATED_RESPONSE_LIMIT" if len(raw) > limit else None), limit


def transport_state(http_status: int | None, failure: str | None) -> str:
    """A transport classification, never a platform identity claim."""
    if failure:
        if failure.startswith("TRUNCATED_"):
            return "PARTIAL_RESPONSE"
        if http_status in (401, 403, 429):
            return "BLOCKED_OR_RATE_LIMITED"
        if http_status == 404:
            return "HTTP_404_NOT_PROOF_OF_ABSENCE"
        return "RETRIEVAL_UNRESOLVED"
    if http_status == 200:
        return "HTTP_200_TRANSPORT_ONLY"
    return "RETRIEVAL_UNRESOLVED"


def complete_integer_total(
    rows: Iterable[Mapping[str, object]],
    *,
    expected_keys: set[str],
    field: str,
) -> int | None:
    """Sum a fixed inventory only when every expected key is present and valid.

    Missing/corrupt/unavailable counters never become zero. This is a *version*
    total, not a number of unique people or an institution adoption metric.
    """
    selected: dict[str, int] = {}
    for row in rows:
        key = row.get("key")
        if key not in expected_keys:
            continue
        if not isinstance(key, str) or key in selected:
            return None
        fields = row.get("selected_public_fields")
        value = fields.get(field) if isinstance(fields, dict) else None
        if row.get("http_status") != 200 or row.get("failure") is not None:
            return None
        if type(value) is not int or value < 0:
            return None
        selected[key] = value
    if set(selected) != expected_keys:
        return None
    return sum(selected.values())
