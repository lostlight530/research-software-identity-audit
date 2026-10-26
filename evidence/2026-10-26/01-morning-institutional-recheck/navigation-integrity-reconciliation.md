# Navigation manifest reference reconciliation

The October 25 manifest included the mutable `monitoring/README.md` and `evidence/README.md` navigation files. Adding later dated entries changes those bytes. This correction preserves their previous bytes under [prior-index-snapshots](prior-index-snapshots/) and retargets only those two manifest paths to the fixed copies, retaining the original byte lengths and SHA-256 values

The [original manifest](prior-index-snapshots/artifact-manifest-20261025-original.json), SHA-256 `b462827ff2102b4dd76b9d1a2a3928dd8b13e1e970886a2bed32944712e7d04d`, is retained verbatim. The other manifest entries and all October 25 source/projection bytes remain unchanged. Future global navigation additions do not alter the fixed copies

Source revision: `5a869e305725cc20ec6762cfd58d07d33360c05b`. This is a locator/integrity repair, with zero prospective cells and no research-count correction
