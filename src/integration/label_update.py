"""Replace a unique label in a UTF-8 text file."""
import logging
from pathlib import Path
from documentation import EasyToolError, atomic_write_text, require_file
log = logging.getLogger(__name__)

def update_label(file: Path, old: str, new: str) -> Path:
    file = require_file(file)
    if not old: raise ValueError("Old label must not be empty")
    try: content = file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc: raise EasyToolError(f"Cannot read {file}: {exc}") from exc
    count = content.count(old)
    if count == 0: raise EasyToolError(f"Label not found in {file}: {old!r}")
    if count > 1: raise EasyToolError(f"Label is ambiguous; found {count} occurrences in {file}")
    atomic_write_text(file, content.replace(old, new, 1))
    log.info("Updated label in %s", file); return file
