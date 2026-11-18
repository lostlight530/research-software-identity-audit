"""Offline schema and completeness tests for OpenAIRE identity projections."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from openaire_identity_projection import project_response, scalar


def result(identifier, title, original, source="ZENODO", hosted="ZENODO"):
    return {
        "header": {
            "dri:objIdentifier": {"$": identifier},
            "dri:status": {"$": "UNDER_CURATION"},
        },
        "metadata": {
            "oaf:entity": {
                "oaf:result": {
                    "title": {"$": title},
                    "originalId": {"$": original},
                    "resulttype": {"@classid": "software"},
                    "collectedfrom": {"@name": source},
                    "children": {"instance": {"hostedby": {"@name": hosted},
                        "webresource": {"url": {"$": "https://example.org/record"}}}},
                }
            }
        },
    }


class OpenAIREProjectionTests(unittest.TestCase):
    def test_scalar_wrapper_and_plain_value(self):
        self.assertEqual(scalar({"$": "x"}), "x")
        self.assertEqual(scalar("x"), "x")
        self.assertIsNone(scalar(None))

    def test_preserves_result_identity_and_provider_fields(self):
        payload = {"response": {"header": {"total": {"$": "1"},
            "page": {"$": 1}, "size": {"$": 100}},
            "results": {"result": [result("doi_dedup___::abc", "Project A",
                "oai:zenodo.org:123")]}}}
        out = project_response(payload)
        self.assertEqual(out["result_total"], 1)
        self.assertTrue(out["result_page_complete"])
        self.assertEqual(out["results"][0]["id"], "doi_dedup___::abc")
        self.assertEqual(out["results"][0]["type"], "software")
        self.assertEqual(out["results"][0]["original_id"], "oai:zenodo.org:123")
        self.assertEqual(out["results"][0]["collected_from"], "ZENODO")
        self.assertEqual(out["results"][0]["hosted_by"], "ZENODO")

    def test_multiple_result_ids_are_retained_as_split_not_collapsed(self):
        payload = {"response": {"header": {"total": {"$": 2}, "size": {"$": 100}},
            "results": {"result": [result("id-a", "A", "oai:a"),
                                    result("id-b", "B", "oai:b")]}}}
        out = project_response(payload)
        self.assertTrue(out["result_page_complete"])
        self.assertEqual([x["id"] for x in out["results"]], ["id-a", "id-b"])

    def test_empty_zero_result_is_complete(self):
        out = project_response({"response": {"header": {"total": {"$": "0"}},
            "results": None}})
        self.assertEqual(out["returned_result_count"], 0)
        self.assertTrue(out["result_page_complete"])

    def test_partial_page_is_not_complete(self):
        payload = {"response": {"header": {"total": {"$": "13"}, "size": {"$": 10}},
            "results": {"result": [result("id-a", "A", "oai:a")]}}}
        out = project_response(payload)
        self.assertFalse(out["result_page_complete"])
        self.assertEqual(out["result_total"], 13)


if __name__ == "__main__":
    unittest.main()
