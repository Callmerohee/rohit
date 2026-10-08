"""Create the standard WORM staging layout."""
import logging
from pathlib import Path
from documentation import ensure_directory
log = logging.getLogger(__name__)

def create_worm_folder(path: Path) -> Path:
    root = ensure_directory(path)
    for name in ("incoming", "validated", "delivered", "rejected"): ensure_directory(root / name)
    log.info("WORM folder ready: %s", root); return root
