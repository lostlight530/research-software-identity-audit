from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.check_repository_text_integrity import audit, markdown_targets


class RepositoryTextIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name: str, content: str):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_json_csv_and_relative_link(self):
        self.write("docs/target.md", "# target\n")
        self.write("docs/source.md", "[target](target.md)\n")
        self.write("data.json", '{"ok": true}\n')
        self.write("data.csv", "id,value\n1,ok\n")
        result = audit(self.root, ["docs/target.md", "docs/source.md", "data.json", "data.csv"])
        self.assertEqual(result["error_count"], 0)
        self.assertEqual(result["relative_markdown_targets_checked"], 1)

    def test_broken_relative_link_is_reported(self):
        self.write("docs/source.md", "[missing](missing.md)\n")
        result = audit(self.root, ["docs/source.md"])
        self.assertEqual(result["errors"][0]["kind"], "broken_relative_link")

    def test_invalid_json_is_reported(self):
        self.write("record.json", '{"unterminated":\n')
        result = audit(self.root, ["record.json"])
        self.assertEqual(result["errors"][0]["kind"], "invalid_json")

    def test_ragged_csv_is_reported(self):
        self.write("data.csv", "a,b\n1,2\n3\n")
        result = audit(self.root, ["data.csv"])
        self.assertEqual(result["errors"][0]["kind"], "ragged_csv_row")

    def test_code_fence_and_fragment_links_are_not_path_checked(self):
        text = "# title\n\n[section](#title)\n\n" + "\x60" * 3 + "md\n[example](not-a-real-file.md)\n" + "\x60" * 3 + "\n"
        self.assertEqual(list(markdown_targets(text)), [(3, "#title")])

    def test_root_relative_link_resolves_from_repository_root(self):
        self.write("target.md", "# target\n")
        self.write("docs/source.md", "[target](/target.md)\n")
        result = audit(self.root, ["target.md", "docs/source.md"])
        self.assertEqual(result["error_count"], 0)


if __name__ == "__main__":
    unittest.main()
