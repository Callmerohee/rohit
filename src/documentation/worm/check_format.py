"""Perform conservative file checks before WORM delivery."""
import hashlib, logging
from pathlib import Path
from documentation import EasyToolError, require_file
log = logging.getLogger(__name__)
ALLOWED_SUFFIXES = {".a2l", ".cps", ".hex", ".cfa", ".json", ".zip"}

def check_format(file: Path) -> dict[str, object]:
    file = require_file(file)
    if file.suffix.lower() not in ALLOWED_SUFFIXES: raise EasyToolError(f"Unsupported WORM file type: {file.suffix}")
    size = file.stat().st_size
    if size == 0: raise EasyToolError(f"Empty files cannot be delivered: {file}")
    digest = hashlib.sha256()
    with file.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""): digest.update(chunk)
    result = {"path": str(file), "size": size, "sha256": digest.hexdigest(), "valid": True}
    log.info("Format check passed: %s", result); return result
