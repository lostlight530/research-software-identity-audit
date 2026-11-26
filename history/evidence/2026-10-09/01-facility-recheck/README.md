# Retained October 9 evidence

Exact response bytes are in raw-responses.tar.gz; capture-manifest.json records endpoint, request window, HTTP status, byte count and SHA-256 for every request

The facility group and earlier page-counter group are separate captures. Failed requests with response bytes are preserved, including resolver error pages

[Monitoring record](../../../monitoring/2026-10-09/01-facility-recheck/README.md) · [Capture manifest](capture-manifest.json) · [Collection contract](collection-contract.json) · [Original page-counter source](page-counter-source.json)

Run python tools/check_retained_facility_evidence.py locally. Offline verification is not a GitHub runner result
