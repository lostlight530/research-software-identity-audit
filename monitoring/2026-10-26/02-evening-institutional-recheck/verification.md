# Executed local verification

- `python -B tools/check.py --mode strict`: all ten contract groups passed
- `python -B tools/check_record_paths.py`: zero path/ownership errors
- `python -B -m unittest discover -s tests -v`: 27 tests passed with task-scoped TEMP/TMP; the first run's Windows sandbox temporary-directory permissions failed and the scoped rerun is retained locally
- `python -B tools/check_retained_all.py`: 3,231 retained-evidence checks, zero failures
- Public artifact manifests: October 25 reference reconciliation plus both October 26 packages checked with the existing repository verifier
- Exact proposed paths, canonical IDs, clock separation, source-attempt counts, arithmetic, privacy minimization and relative links checked locally against the pinned base

The public package contains selected fields and local response digests. Original response bodies are retained locally. These checks establish patch structure and arithmetic, without asserting source authenticity or scientific validation. Cloud CI/review is not claimed executed
