"""Generate a deterministic SHA-256 resource manifest."""
import hashlib, json, logging
from pathlib import Path
from documentation import atomic_write_text, require_directory
log = logging.getLogger(__name__)

def generate_resources(source: Path, output: Path) -> Path:
    source = require_directory(source); output = Path(output).expanduser().resolve()
    records = []
    for file in sorted(p for p in source.rglob("*") if p.is_file()):
        digest = hashlib.sha256()
        with file.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""): digest.update(chunk)
        records.append({"path": file.relative_to(source).as_posix(), "size": file.stat().st_size, "sha256": digest.hexdigest()})
    atomic_write_text(output, json.dumps({"resources": records}, indent=2) + "\n")
    log.info("Generated manifest for %d resources: %s", len(records), output); return output
