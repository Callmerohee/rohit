"""Safely merge JSON updates into a JSON project configuration file."""
import json, logging
from pathlib import Path
from documentation import EasyToolError, atomic_write_text, load_json, require_file
log = logging.getLogger(__name__)

def _deep_merge(base: dict, updates: dict) -> dict:
    for key, value in updates.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict): _deep_merge(base[key], value)
        else: base[key] = value
    return base

def update_project_config(config_file: Path, updates_file: Path) -> Path:
    config_file = require_file(config_file, suffix=".json")
    log.info("Updating project configuration %s with %s", config_file, updates_file)
    merged = _deep_merge(load_json(config_file), load_json(updates_file))
    try: payload = json.dumps(merged, indent=2, sort_keys=True) + "\n"
    except (TypeError, ValueError) as exc: raise EasyToolError(f"Configuration is not JSON serializable: {exc}") from exc
    atomic_write_text(config_file, payload)
    log.info("Configuration updated: %s", config_file); return config_file
