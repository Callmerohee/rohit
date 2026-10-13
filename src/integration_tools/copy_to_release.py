"""Copy to Release GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_copy_to_release() -> None:
    """Implement the Copy to Release business logic here."""
    not_implemented("Copy to Release")


def open_copy_to_release(parent: tk.Misc) -> None:
    """Open the Copy to Release dialog."""
    LOGGER.debug("Opening Copy to Release dialog")
    window = tk.Toplevel(parent)
    window.title("Copy to Release")
    window.geometry("420x190")
    window.transient(parent)

    frame = ttk.Frame(window, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Copy to Release", font=("Segoe UI", 14, "bold")).pack(pady=(0, 10))
    ttk.Label(
        frame,
        text="Add input controls and business logic in:\nintegration_tools/copy_to_release.py",
        justify="center",
    ).pack(pady=5)
    ttk.Button(
        frame,
        text="Run",
        command=lambda: run_gui_action("Copy to Release", execute_copy_to_release),
    ).pack(pady=12)
