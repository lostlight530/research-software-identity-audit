# Local source bundle — transport and byte boundaries

This package is paired with [the dated handoff](../../../monitoring/2026-10-24/04-local-history-evidence-handoff/README.md). The [ledger](local-source-ledger.json) is gzip-csv-base64-v1 and maps original relative local artifacts to SHA-256-addressed public objects. Decode, check gzip_sha256 and decompress that CSV. The [attempt manifest](capture-manifest.json) is plain JSON, specifies the exact public-field/host/query allowlists, and links plain public-attempts-NN.jsonl projections. Original full logs, error messages, headers and private query parameters are not published. Clocks and outcomes stay attributed to their original source; repeated rows across retained logs are not counted as distinct requests. Missing HTTP Date/response headers and unretained responses are not reconstructed.

There are 14 UTF-8 source-bundle-part-NN.json files. Each has format gzip-tar-base64-v1, data_base64, gzip_sha256 and member_count. Decode each data_base64, verify the compressed SHA-256, decompress gzip and read the tar **without executing members**. Members are regular files named objects/<64-hex-sha256>.bin. Verify each payload against its filename digest; use the ledger's original source extension to interpret JSON/CSV. Parts are independent and must not be concatenated as one gzip archive.

`published_byte_preserved` means exact original local bytes. `published_minimized_projection` means incidental personal/credential/telemetry/local-path data was removed and the original SHA differs; it is not raw HTTP proof. Omitted or cloud-identical artifacts remain explicit ledger rows. Every original stays local; no old evidence package is rewritten. Existing source labels and historical interpretations are not silently corrected inside archived originals.

Basic decode example (read-only):

```python
import base64, gzip, hashlib, io, json, tarfile
from pathlib import Path
for path in sorted(Path('.').glob('source-bundle-part-*.json')):
    part = json.loads(path.read_text(encoding='utf-8'))
    compressed = base64.b64decode(part['data_base64'], validate=True)
    assert hashlib.sha256(compressed).hexdigest() == part['gzip_sha256']
    with tarfile.open(fileobj=io.BytesIO(gzip.decompress(compressed)), mode='r:') as archive:
        for member in archive.getmembers():
            assert member.isfile() and member.name.startswith('objects/')
            body = archive.extractfile(member).read()
            assert hashlib.sha256(body).hexdigest() == Path(member.name).stem
```

This example is a transfer-integrity check, not a source interpretation review or a newly installed CI job. Review the source-file ledger and timestamps before using any numeric series. No human audience, referrer or causal claim is added.
