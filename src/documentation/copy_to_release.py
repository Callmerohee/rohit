"""Copy a file or directory to a release location."""
import logging, shutil
from pathlib import Path
from documentation import EasyToolError, ensure_directory
log = logging.getLogger(__name__)

def copy_to_release(source: Path, destination: Path) -> Path:
    source = Path(source).expanduser().resolve(); destination = Path(destination).expanduser().resolve()
    if not source.exists(): raise FileNotFoundError(f"Source does not exist: {source}")
    if source == destination: raise EasyToolError("Source and destination must differ")
    ensure_directory(destination.parent)
    try:
        if source.is_dir():
            if destination.exists(): raise EasyToolError(f"Release destination already exists: {destination}")
            shutil.copytree(source, destination)
        else: shutil.copy2(source, destination)
    except OSError as exc: raise EasyToolError(f"Release copy failed: {exc}") from exc
    log.info("Copied release artifact to %s", destination); return destination
