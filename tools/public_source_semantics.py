"""Conservative, network-free public surface identity projections.

Operate only on a *new, complete, bounded* response body. Never use these
functions to rewrite a historical source attempt, assert independent uptake,
or infer that a failed/blocked/404 request means object absence.

The outputs are intentionally small public metadata projections, not raw
provider evidence. No credentials, private contacts, or source body are kept.
"""
from __future__ import annotations

import json
from xml.etree import ElementTree as ET

SEMANTIC_SURFACE_KEYS = frozenset({
    "06:bio.tools", "07:OpenEBench", "15:EDAM",
    "27:Handle DOI", "28:Crossref agency", "31:CiteAs",
})
_EXPECTED_TOOL_HOME = (
    "https://github.com/lostlight530/life-science-ecosystem-lab/tree/main/bio_tool"
)
_EXPECTED_CITE_URL = "https://github.com/lostlight530/welcome-to-github"
_EXPECTED_OSF_HANDLE = "10.17605/osf.io/5b329"
_EXPECTED_EDAM_TERMS = (
    "operation_2403", "operation_2406", "data_2976", "data_2955",
    "data_1460", "format_1929", "format_1476", "topic_0078", "topic_0080",
)
_MAX_JSON_BYTES = 2_000_000
_MAX_EDAM_BYTES = 4 * 1024 * 1024


def _unknown(reason: str) -> dict[str, object]:
    return {"semantic_identity_status": "TARGET_UNKNOWN", "reason": reason}


def _project_json(key: str, obj: object) -> dict[str, object]:
    if not isinstance(obj, dict):
        return _unknown("JSON_NOT_OBJECT")

    if key == "06:bio.tools":
        ident = obj.get("biotoolsID")
        homepage = obj.get("homepage")
        if ident != "life-science-protein-file-audit" or homepage != _EXPECTED_TOOL_HOME:
            return _unknown("BIOTOOLS_ID_OR_HOMEPAGE_MISMATCH")
        versions = obj.get("version")
        return {
            "semantic_identity_status": "EXACT_TOOL_RECORD_MATCH",
            "biotools_id": ident,
            "biotools_curie": obj.get("biotoolsCURIE"),
            "homepage": homepage,
            "record_version_labels": [v for v in versions if isinstance(v, str)][:10]
                if isinstance(versions, list) else [],
            "validated_value": obj.get("validated"),
            "identity_boundary": "registry_metadata_not_current_release_or_tool_validation",
        }

    if key == "07:OpenEBench":
        ident = obj.get("@id")
        label = obj.get("@label")
        home = (obj.get("web") or {}).get("homepage") if isinstance(obj.get("web"), dict) else None
        if (ident != "https://openebench.bsc.es/monitor/tool/life-science-protein-file-audit"
                or label != "life-science-protein-file-audit"
                or home != _EXPECTED_TOOL_HOME):
            return _unknown("MONITOR_ID_LABEL_OR_HOMEPAGE_MISMATCH")
        return {
            "semantic_identity_status": "EXACT_MONITOR_TOOL_METADATA_MATCH",
            "tool_id": ident, "label": label,
            "homepage": home, "provider_timestamp": obj.get("@timestamp"),
            "validated_value": obj.get("validated"),
            "identity_boundary": "monitor_metadata_not_scientific_benchmark_execution",
        }

    if key == "27:Handle DOI":
        handle = obj.get("handle")
        values = obj.get("values")
        if obj.get("responseCode") != 1 or not isinstance(handle, str) or (
                handle.lower() != _EXPECTED_OSF_HANDLE) or not isinstance(values, list):
            return _unknown("HANDLE_RESPONSE_OR_IDENTIFIER_MISMATCH")
        urls = [v.get("data", {}).get("value")
                for v in values if isinstance(v, dict) and v.get("type") == "URL"
                and isinstance(v.get("data"), dict)
                and isinstance(v["data"].get("value"), str)]
        if "https://osf.io/5b329/" not in urls:
            return _unknown("EXPECTED_OSF_URL_NOT_IN_HANDLE_VALUES")
        return {
            "semantic_identity_status": "HANDLE_URL_MAPPING_VERIFIED",
            "handle": handle, "url": "https://osf.io/5b329/",
            "identity_boundary": "identifier_resolution_not_registration_content_validation",
        }

    if key == "28:Crossref agency":
        message = obj.get("message")
        if obj.get("status") != "ok" or not isinstance(message, dict):
            return _unknown("CROSSREF_AGENCY_RESPONSE_NOT_OK")
        agency = message.get("agency")
        doi = message.get("DOI")
        if (not isinstance(doi, str) or doi.lower() != _EXPECTED_OSF_HANDLE
                or not isinstance(agency, dict) or agency.get("id") != "datacite"):
            return _unknown("DOI_OR_AGENCY_MISMATCH")
        return {
            "semantic_identity_status": "DOI_REGISTRATION_AGENCY_IDENTIFIED",
            "doi": doi.lower(), "agency_id": agency["id"],
            "agency_label": agency.get("label"),
            "identity_boundary": "agency_lookup_not_crossref_work_registration",
        }

    if key == "31:CiteAs":
        metadata = obj.get("metadata")
        if not isinstance(metadata, dict):
            return _unknown("CITEAS_METADATA_MISSING")
        doi = metadata.get("DOI")
        if (obj.get("name") != "welcome-to-github"
                or obj.get("url") != _EXPECTED_CITE_URL
                or not isinstance(doi, str) or doi.lower() != "10.5281/zenodo.22790907"
                or metadata.get("type") != "software"):
            return _unknown("CITEAS_REPOSITORY_OR_DOI_MISMATCH")
        return {
            "semantic_identity_status": "CITATION_METADATA_RECORD_MATCH",
            "repository_url": obj["url"], "software_name": obj["name"],
            "doi": doi.lower(), "metadata_version": metadata.get("version"),
            "metadata_type": "software",
            "identity_boundary": "citation_metadata_not_citation_use_or_quality_endorsement",
        }

    return _unknown("UNSUPPORTED_SURFACE")


def _project_edam(raw: bytes) -> dict[str, object]:
    root = ET.fromstring(raw)
    if root.tag != "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF":
        return _unknown("NOT_RDF_XML")
    owl = "{http://www.w3.org/2002/07/owl#}"
    rdf_about = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"
    rdfs_label = "{http://www.w3.org/2000/01/rdf-schema#}label"
    ontology = root.find(owl + "Ontology")
    if ontology is None:
        return _unknown("OWL_ONTOLOGY_NODE_MISSING")
    ontology_uri = ontology.get(rdf_about)
    if ontology_uri not in {"http://edamontology.org", "http://edamontology.org/"}:
        return _unknown("EDAM_ONTOLOGY_URI_MISMATCH")
    version_node = ontology.find(owl + "versionInfo")
    version = (version_node.text or "").strip() if version_node is not None else None
    targets = {"http://edamontology.org/" + k: k for k in _EXPECTED_EDAM_TERMS}
    terms: dict[str, str | None] = {}
    for item in root.iter(owl + "Class"):
        uri = item.get(rdf_about)
        if uri in targets:
            label = item.find(rdfs_label)
            terms[targets[uri]] = (label.text or "").strip() if label is not None else None
    return {
        "semantic_identity_status": "EDAM_ONTOLOGY_RETRIEVED",
        "ontology_uri": ontology_uri,
        "ontology_version": version,
        "expected_term_count": len(_EXPECTED_EDAM_TERMS),
        "matched_term_count": len(terms),
        "matched_terms": terms,
        "identity_boundary": "vocabulary_metadata_not_software_listing_or_exact_term_mapping_validation",
    }


def project_surface(
    key: str, raw: bytes, *, http_status: int | None, failure: str | None
) -> dict[str, object]:
    """Project selected fields; unknown stays unknown and blocked stays blocked.

    Unknown keys return {} so callers can retain their existing parser behavior.
    """
    if key not in SEMANTIC_SURFACE_KEYS:
        return {}
    if http_status != 200 or failure:
        return {
            "semantic_identity_status": "NOT_VERIFIED_TRANSPORT",
            "transport_or_read_failure": failure or "HTTP_NON_200",
        }
    limit = _MAX_EDAM_BYTES if key == "15:EDAM" else _MAX_JSON_BYTES
    if not isinstance(raw, bytes) or not raw or len(raw) > limit:
        return _unknown("EMPTY_NON_BYTES_OR_OVERSIZE_RESPONSE")
    try:
        if key == "15:EDAM":
            return _project_edam(raw)
        obj = json.loads(raw)
        return _project_json(key, obj)
    except (ValueError, TypeError, ET.ParseError) as exc:
        return {
            "semantic_identity_status": "PARSE_FAILED",
            "parse_kind": type(exc).__name__,
        }
