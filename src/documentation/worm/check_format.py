"""Check Format GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_check_format() -> None:
    """Implement the Check Format business logic here."""
    not_implemented("Check Format")


def open_check_format(parent: tk.Misc) -> None:
    """Open the Check Format dialog."""
    LOGGER.debug("Opening Check Format dialog")
    window = tk.Toplevel(parent)
    window.title("Check Format")
    window.geometry("420x190")
    window.transient(parent)

    frame = ttk.Frame(window, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Check Format", font=("Segoe UI", 14, "bold")).pack(pady=(0, 10))
    ttk.Label(
        frame,
        text="Add input controls and business logic in:\ndocumentation/worm/check_format.py",
        justify="center",
    ).pack(pady=5)
    ttk.Button(
        frame,
        text="Run",
        command=lambda: run_gui_action("Check Format", execute_check_format),
    ).pack(pady=12)
