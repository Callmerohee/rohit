"""Create a view by copying a source tree to a new destination."""
import logging, shutil
from pathlib import Path
from documentation import EasyToolError, require_directory
log = logging.getLogger(__name__)

def create_view(source: Path, destination: Path) -> Path:
    source = require_directory(source); destination = Path(destination).expanduser().resolve()
    log.info("Creating view from %s to %s", source, destination)
    if destination.exists(): raise EasyToolError(f"Destination already exists: {destination}")
    try: shutil.copytree(source, destination)
    except OSError as exc:
        shutil.rmtree(destination, ignore_errors=True)
        raise EasyToolError(f"View creation failed: {exc}") from exc
    log.info("View created: %s", destination); return destination
