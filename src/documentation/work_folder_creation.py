"""Create the standard work-folder layout."""
import logging
from pathlib import Path
from documentation import ensure_directory
log = logging.getLogger(__name__)

def create_work_folder(path: Path) -> Path:
    root = ensure_directory(path)
    for name in ("input", "output", "temp", "archive"): ensure_directory(root / name)
    log.info("Work folder ready: %s", root); return root
