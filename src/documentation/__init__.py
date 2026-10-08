"""Shared documentation/workflow utilities."""
from __future__ import annotations

import json
import logging
import os
import shutil
import tempfile
from pathlib import Path
from typing import Any

class EasyToolError(RuntimeError):
    """Base exception for expected EasyTool failures."""


def require_file(path: Path, *, suffix: str | None = None) -> Path:
    path = Path(path).expanduser().resolve()
    if not path.exists(): raise FileNotFoundError(f"File does not exist: {path}")
    if not path.is_file(): raise EasyToolError(f"Expected a file: {path}")
    if suffix and path.suffix.lower() != suffix.lower():
        raise EasyToolError(f"Expected a {suffix} file, received: {path.name}")
    return path


def require_directory(path: Path) -> Path:
    path = Path(path).expanduser().resolve()
    if not path.exists(): raise FileNotFoundError(f"Directory does not exist: {path}")
    if not path.is_dir(): raise EasyToolError(f"Expected a directory: {path}")
    return path


def ensure_directory(path: Path) -> Path:
    path = Path(path).expanduser().resolve()
    try: path.mkdir(parents=True, exist_ok=True)
    except OSError as exc: raise EasyToolError(f"Cannot create directory {path}: {exc}") from exc
    return path


def load_json(path: Path) -> dict[str, Any]:
    path = require_file(path, suffix=".json")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise EasyToolError(f"Cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(data, dict): raise EasyToolError(f"JSON root must be an object: {path}")
    return data


def atomic_write_text(path: Path, content: str) -> Path:
    path = Path(path).expanduser().resolve()
    ensure_directory(path.parent)
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as tmp:
            tmp.write(content); tmp.flush(); os.fsync(tmp.fileno()); temp_name = tmp.name
        os.replace(temp_name, path)
        return path
    except OSError as exc:
        raise EasyToolError(f"Cannot write {path}: {exc}") from exc
    finally:
        if temp_name and os.path.exists(temp_name): os.unlink(temp_name)


def atomic_copy(source: Path, destination: Path) -> Path:
    source = require_file(source)
    destination = Path(destination).expanduser().resolve()
    ensure_directory(destination.parent)
    temp = destination.with_name(destination.name + ".tmp")
    try:
        shutil.copy2(source, temp); os.replace(temp, destination); return destination
    except OSError as exc:
        raise EasyToolError(f"Cannot copy {source} to {destination}: {exc}") from exc
    finally:
        temp.unlink(missing_ok=True)
