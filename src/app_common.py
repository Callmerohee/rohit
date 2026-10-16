"""Shared logging, error handling, and GUI helpers for EasyTool."""
from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from tkinter import messagebox
from typing import Callable, TypeVar

APP_ROOT = Path(__file__).resolve().parent
LOG_DIR = APP_ROOT / "log"
LOG_FILE = LOG_DIR / "Log.txt"
T = TypeVar("T")


class EasyToolError(Exception):
    """Base exception for expected EasyTool errors."""


def configure_logging() -> None:
    """Configure rotating file logging and console logging once."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger()
    if logger.handlers:
        return
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s"
    )
    LOG_FILE.write_text("", encoding="utf-8")
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=2_000_000, backupCount=5, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def run_gui_action(action_name: str, action: Callable[[], T]) -> T | None:
    """Execute a GUI callback with consistent logging and user-safe errors."""
    logger = logging.getLogger(action.__module__)
    logger.info("Started: %s", action_name)
    try:
        result = action()
    except EasyToolError as exc:
        logger.warning("Expected failure in %s: %s", action_name, exc)
        messagebox.showwarning(action_name, str(exc))
    except (FileNotFoundError, PermissionError, ValueError) as exc:
        logger.error("Input or file error in %s: %s", action_name, exc, exc_info=True)
        messagebox.showerror(action_name, str(exc))
    except Exception as exc:
        logger.exception("Unexpected failure in %s", action_name)
        messagebox.showerror(
            action_name,
            f"An unexpected error occurred: {exc}\nSee log/Log.txt for details.",
        )
    else:
        logger.info("Completed: %s", action_name)
        return result
    return None


def not_implemented(feature_name: str) -> None:
    """Standard placeholder used until feature logic is implemented."""
    logging.getLogger(__name__).info("Placeholder opened: %s", feature_name)
    messagebox.showinfo(
        feature_name,
        "The GUI connection, logging, and error handling are ready. "
        "Add the feature logic in its module.",
    )
