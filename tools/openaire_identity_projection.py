"""Minimal OpenAIRE Search API identity projection for bounded diagnostics.

The projection preserves the query DOI separately from OpenAIRE result identity.
It does not equate a DOI query, result occurrence, result ID, or repository.
"""
from __future__ import annotations

from typing import Any


def scalar(value: Any) -> Any:
    """Unwrap OAF scalar wrappers without flattening unrelated structures."""
    if isinstance(value, dict) and "$" in value:
        return value["$"]
    return value


def _items(value: Any) -> list[dict[str, Any]]:
    if value is None:
        return []
    if isinstance(value, dict):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    return []


def _name(value: Any) -> Any:
    if isinstance(value, dict):
        return scalar(value.get("@name") or value.get("$"))
    return scalar(value)


def project_response(payload: dict[str, Any]) -> dict[str, Any]:
    """Return stable selected fields from one OpenAIRE exact-DOI response.

    A query is complete only if every result reported by the response header
    is present in this page. The collector requests size=100; any larger result
    set remains explicitly incomplete rather than being silently truncated.
    """
    response = payload.get("response") or {}
    header = response.get("header") or {}
    total_value = scalar(header.get("total"))
    try:
        total = int(total_value)
    except (TypeError, ValueError):
        total = None
    page = scalar(header.get("page"))
    page_size = scalar(header.get("size"))

    results_box = response.get("results") or {}
    raw_results = results_box.get("result") if isinstance(results_box, dict) else None
    projected: list[dict[str, Any]] = []
    for item in _items(raw_results):
        item_header = item.get("header") or {}
        metadata = item.get("metadata") or {}
        entity = metadata.get("oaf:entity") or {}
        result = entity.get("oaf:result") or entity.get("oaf:software") or {}
        result_type = result.get("resulttype") or {}
        children = result.get("children") or {}
        instances = _items(children.get("instance"))
        instance = instances[0] if instances else {}
        webresource = instance.get("webresource") or {}
        web_url = scalar((webresource.get("url") or {}))
        projected.append({
            "id": scalar((item_header.get("dri:objIdentifier") or {})),
            "type": result_type.get("@classid") or scalar(result_type),
            "title": scalar(result.get("title")),
            "original_id": scalar(result.get("originalId")),
            "collected_from": _name(result.get("collectedfrom")),
            "hosted_by": _name(instance.get("hostedby")),
            "source_status": scalar(item_header.get("dri:status")),
            "record_url": web_url,
        })

    complete = (total == 0 and len(projected) == 0) or (
        total is not None and total == len(projected)
    )
    return {
        "result_total": total,
        "returned_result_count": len(projected),
        "page": page,
        "page_size": page_size,
        "result_page_complete": complete,
        "results": projected,
    }
