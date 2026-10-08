"""Create a small SQLite diagnostic database from JSON records."""
import json, logging, sqlite3
from pathlib import Path
from documentation import EasyToolError, ensure_directory, require_file
log = logging.getLogger(__name__)

def create_diagdb(source: Path, output: Path) -> Path:
    source = require_file(source, suffix=".json"); output = Path(output).expanduser().resolve()
    ensure_directory(output.parent)
    try:
        records = json.loads(source.read_text(encoding="utf-8"))
        if not isinstance(records, list): raise EasyToolError("Diagnostic JSON must contain a list")
        with sqlite3.connect(output) as db:
            db.execute("CREATE TABLE IF NOT EXISTS diagnostics (id INTEGER PRIMARY KEY, payload TEXT NOT NULL)")
            db.execute("DELETE FROM diagnostics")
            db.executemany("INSERT INTO diagnostics(payload) VALUES (?)", [(json.dumps(r, sort_keys=True),) for r in records])
    except (OSError, UnicodeError, json.JSONDecodeError, sqlite3.Error) as exc:
        output.unlink(missing_ok=True); raise EasyToolError(f"Diagnostic DB creation failed: {exc}") from exc
    log.info("Created diagnostic DB with %d records: %s", len(records), output); return output
