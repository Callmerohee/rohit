"""File patching helpers."""
from __future__ import annotations
import logging
from pathlib import Path
from documentation import EasyToolError, atomic_write_text, require_file
log = logging.getLogger(__name__)

def patch_text_file(source: Path, output: Path, expected_suffix: str, marker: str) -> Path:
    source = require_file(source, suffix=expected_suffix)
    output = Path(output).expanduser().resolve()
    try: content = source.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc: raise EasyToolError(f"Cannot read {source} as UTF-8 text: {exc}") from exc
    if marker in content: raise EasyToolError(f"File already contains patch marker: {marker}")
    atomic_write_text(output, content.rstrip() + f"\n{marker}\n")
    log.info("Patched %s -> %s", source, output); return output
