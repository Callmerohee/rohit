"""Validate and atomically deliver one file to a WORM destination."""
import logging
from pathlib import Path
from documentation import EasyToolError, atomic_copy, ensure_directory
from documentation.worm.check_format import check_format
log = logging.getLogger(__name__)

def deliver_to_worm(source: Path, destination: Path) -> Path:
    metadata = check_format(source)
    destination = Path(destination).expanduser().resolve()
    if destination.exists(): raise EasyToolError(f"WORM destination is immutable and already exists: {destination}")
    ensure_directory(destination.parent)
    delivered = atomic_copy(Path(str(metadata["path"])), destination)
    check = check_format(delivered)
    if check["sha256"] != metadata["sha256"]:
        delivered.unlink(missing_ok=True); raise EasyToolError("Checksum mismatch after WORM delivery")
    log.info("Delivered immutable artifact: %s", delivered); return delivered
