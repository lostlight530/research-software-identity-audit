"""Network-free and fail-closed tests for source-specific public identity projection."""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from public_source_semantics import project_surface, SEMANTIC_SURFACE_KEYS


def project(key, payload):
    return project_surface(key, json.dumps(payload).encode(), http_status=200, failure=None)


class PublicSourceSemanticTests(unittest.TestCase):
    def test_exact_biotools_record_does_not_claim_validation(self):
        got = project("06:bio.tools", {
            "biotoolsID": "life-science-protein-file-audit",
            "biotoolsCURIE": "biotools:life-science-protein-file-audit",
            "homepage": "https://github.com/lostlight530/life-science-ecosystem-lab/tree/main/bio_tool",
            "version": ["0.4.0"], "validated": 0,
            "credit": [{"email": "DO_NOT_STORE@example.invalid"}],
        })
        self.assertEqual(got["semantic_identity_status"], "EXACT_TOOL_RECORD_MATCH")
        self.assertEqual(got["record_version_labels"], ["0.4.0"])
        self.assertEqual(got["validated_value"], 0)
        self.assertNotIn("email", str(got))
        self.assertNotIn("0.5.1", str(got))

    def test_biotools_mismatch_not_discoverable(self):
        got = project("06:bio.tools", {"biotoolsID": "different", "homepage": "bad"})
        self.assertEqual(got["semantic_identity_status"], "TARGET_UNKNOWN")

    def test_openebench_not_benchmark(self):
        got = project("07:OpenEBench", {
            "@id": "https://openebench.bsc.es/monitor/tool/life-science-protein-file-audit",
            "@label": "life-science-protein-file-audit",
            "web": {"homepage": "https://github.com/lostlight530/life-science-ecosystem-lab/tree/main/bio_tool"},
            "@timestamp": "2026-11-18T00:00:00Z", "validated": 0,
        })
        self.assertEqual(got["semantic_identity_status"], "EXACT_MONITOR_TOOL_METADATA_MATCH")
        self.assertIn("not_scientific_benchmark", got["identity_boundary"])

    def test_handle_selects_url_not_admin(self):
        got = project("27:Handle DOI", {
            "responseCode": 1, "handle": "10.17605/osf.io/5b329",
            "values": [{"type": "HS_ADMIN", "data": {"value": {"permissions": "private"}}},
                       {"type": "URL", "data": {"value": "https://osf.io/5b329/"}}],
        })
        self.assertEqual(got["semantic_identity_status"], "HANDLE_URL_MAPPING_VERIFIED")
        self.assertEqual(got["url"], "https://osf.io/5b329/")
        self.assertNotIn("permissions", str(got))

    def test_handle_wrong_target_is_unknown(self):
        got = project("27:Handle DOI", {"responseCode": 1,
            "handle": "10.17605/osf.io/5b329",
            "values": [{"type": "URL", "data": {"value": "https://other.invalid"}}]})
        self.assertEqual(got["semantic_identity_status"], "TARGET_UNKNOWN")

    def test_crossref_agency_does_not_mean_crossref_registration(self):
        got = project("28:Crossref agency", {"status": "ok", "message": {
            "DOI": "10.17605/OSF.IO/5B329", "agency": {"id": "datacite", "label": "DataCite"}}})
        self.assertEqual(got["agency_id"], "datacite")
        self.assertIn("not_crossref_work_registration", got["identity_boundary"])

    def test_citeas_reference_not_citation_event(self):
        got = project("31:CiteAs", {
            "name": "welcome-to-github",
            "url": "https://github.com/lostlight530/welcome-to-github",
            "metadata": {"DOI": "10.5281/ZENODO.22790907",
                         "type": "software", "version": "v2026.11-ten-day-evidence-checkpoint"},
            "provenance": [{"secret": "DO_NOT_RETAIN"}],
        })
        self.assertEqual(got["doi"], "10.5281/zenodo.22790907")
        self.assertNotIn("secret", str(got))

    def test_edam_rdf_xml_is_not_json_and_has_bounded_labels(self):
        raw = b'''<?xml version="1.0"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">
<owl:Ontology rdf:about="http://edamontology.org/">
  <owl:versionInfo>1.25-20260626T1230Z</owl:versionInfo>
</owl:Ontology>
<owl:Class rdf:about="http://edamontology.org/operation_2403">
  <rdfs:label>Sequence analysis</rdfs:label>
</owl:Class>
<owl:Class rdf:about="http://edamontology.org/operation_9999">
  <rdfs:label>Out of scope</rdfs:label>
</owl:Class>
</rdf:RDF>'''
        got = project_surface("15:EDAM", raw, http_status=200, failure=None)
        self.assertEqual(got["semantic_identity_status"], "EDAM_ONTOLOGY_RETRIEVED")
        self.assertEqual(got["matched_term_count"], 1)
        self.assertEqual(got["ontology_version"], "1.25-20260626T1230Z")
        self.assertNotIn("operation_9999", str(got))

    def test_edam_mismatch_or_invalid_xml_not_success(self):
        self.assertEqual(project_surface("15:EDAM", b"<html/>",
            http_status=200, failure=None)["semantic_identity_status"], "TARGET_UNKNOWN")
        self.assertEqual(project_surface("15:EDAM", b"<rdf:RDF",
            http_status=200, failure=None)["semantic_identity_status"], "PARSE_FAILED")

    def test_failure_and_unsupported_keys_remain_unresolved(self):
        self.assertEqual(project_surface("14:InterLex", b"{}",
            http_status=403, failure="HTTP_403"), {})
        self.assertEqual(project_surface("31:CiteAs", b'{"name":"welcome-to-github"}',
            http_status=403, failure="HTTP_403")["semantic_identity_status"], "NOT_VERIFIED_TRANSPORT")
        self.assertEqual(project_surface("15:EDAM", b"{}", http_status=200,
            failure="TRUNCATED_RESPONSE_LIMIT")["semantic_identity_status"], "NOT_VERIFIED_TRANSPORT")
        self.assertEqual(project_surface("27:Handle DOI", b"x" * 2_000_001,
            http_status=200, failure=None)["semantic_identity_status"], "TARGET_UNKNOWN")
        self.assertEqual(len(SEMANTIC_SURFACE_KEYS), 6)


if __name__ == "__main__":
    unittest.main()
