"""EasyTool command-line entry point."""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Callable

from documentation import EasyToolError
from documentation.copy_to_release import copy_to_release
from documentation.diagdb_creation import create_diagdb
from documentation.resource_generation import generate_resources
from documentation.work_folder_creation import create_work_folder
from documentation.worm_folder_creation import create_worm_folder
from documentation.patching.a2l import patch_a2l
from documentation.patching.cfa import patch_cfa
from documentation.patching.cps import patch_cps
from documentation.patching.hex import patch_hex
from documentation.worm.check_format import check_format
from documentation.worm.deliver_to_worm import deliver_to_worm
from integration.label_update import update_label
from integration.update_configuration import update_configuration
from integration.update_project_config import update_project_config
from integration.view_creation import create_view

LOG_DIR = Path(__file__).resolve().parent / "log"
LOG_FILE = LOG_DIR / "Log.txt"


def configure_logging(verbose: bool = False) -> None:
    """Configure console and UTF-8 file logging once."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    level = logging.DEBUG if verbose else logging.INFO
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s"
    )
    root = logging.getLogger()
    root.setLevel(level)
    root.handlers.clear()

    console = logging.StreamHandler(sys.stdout)
    console.setLevel(level)
    console.setFormatter(formatter)
    root.addHandler(console)

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="EasyTool automation utility")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    sub = parser.add_subparsers(dest="command", required=True)

    def path_cmd(name: str, help_text: str, *args: tuple[str, str]) -> None:
        p = sub.add_parser(name, help=help_text)
        for flag, description in args:
            p.add_argument(flag, required=True, type=Path, help=description)

    path_cmd("create-view", "Create an integration view", ("--source", "Source directory"), ("--destination", "View directory"))
    path_cmd("update-configuration", "Update a configuration file", ("--file", "Configuration file"), ("--updates", "JSON updates file"))
    path_cmd("update-project-config", "Update project configuration", ("--file", "Project config file"), ("--updates", "JSON updates file"))
    p = sub.add_parser("update-label", help="Update a label in a text file")
    p.add_argument("--file", required=True, type=Path); p.add_argument("--old", required=True); p.add_argument("--new", required=True)
    path_cmd("create-work-folder", "Create work folder", ("--path", "Folder path"))
    path_cmd("copy-to-release", "Copy output to release", ("--source", "Source"), ("--destination", "Release destination"))
    path_cmd("create-diagdb", "Create diagnostic database", ("--source", "Input file"), ("--output", "Output database"))
    path_cmd("generate-resources", "Generate resource manifest", ("--source", "Resource directory"), ("--output", "Manifest file"))
    path_cmd("create-worm-folder", "Create WORM folder", ("--path", "Folder path"))
    for ext in ("a2l", "cps", "hex", "cfa"):
        path_cmd(f"patch-{ext}", f"Patch {ext.upper()} file", ("--source", "Source file"), ("--output", "Output file"))
    path_cmd("check-format", "Validate WORM input format", ("--file", "File to validate"))
    path_cmd("deliver-to-worm", "Deliver file to WORM", ("--source", "Source file"), ("--destination", "WORM destination"))
    return parser


def dispatch(args: argparse.Namespace) -> object:
    commands: dict[str, Callable[[], object]] = {
        "create-view": lambda: create_view(args.source, args.destination),
        "update-configuration": lambda: update_configuration(args.file, args.updates),
        "update-project-config": lambda: update_project_config(args.file, args.updates),
        "update-label": lambda: update_label(args.file, args.old, args.new),
        "create-work-folder": lambda: create_work_folder(args.path),
        "copy-to-release": lambda: copy_to_release(args.source, args.destination),
        "create-diagdb": lambda: create_diagdb(args.source, args.output),
        "generate-resources": lambda: generate_resources(args.source, args.output),
        "create-worm-folder": lambda: create_worm_folder(args.path),
        "patch-a2l": lambda: patch_a2l(args.source, args.output),
        "patch-cps": lambda: patch_cps(args.source, args.output),
        "patch-hex": lambda: patch_hex(args.source, args.output),
        "patch-cfa": lambda: patch_cfa(args.source, args.output),
        "check-format": lambda: check_format(args.file),
        "deliver-to-worm": lambda: deliver_to_worm(args.source, args.destination),
    }
    return commands[args.command]()


def main() -> int:
    args = build_parser().parse_args()
    configure_logging(args.verbose)
    log = logging.getLogger(__name__)
    try:
        result = dispatch(args)
        log.info("Command '%s' completed successfully: %s", args.command, result)
        return 0
    except (EasyToolError, ValueError, FileNotFoundError, PermissionError) as exc:
        log.error("Command '%s' failed: %s", args.command, exc, exc_info=args.verbose)
        return 2
    except KeyboardInterrupt:
        log.warning("Operation cancelled by user")
        return 130
    except Exception:
        log.exception("Unexpected failure while running command '%s'", args.command)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
