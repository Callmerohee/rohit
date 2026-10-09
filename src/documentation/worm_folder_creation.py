"""WORM Folder Creation GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_worm_folder_creation() -> None:
    """Implement the WORM Folder Creation business logic here."""
    not_implemented("WORM Folder Creation")


def open_worm_folder_creation(parent: tk.Misc) -> None:
    """Open the WORM Folder Creation dialog."""
    LOGGER.debug("Opening WORM Folder Creation dialog")
    window = tk.Toplevel(parent)
    window.title("WORM Folder Creation")
    window.geometry("420x190")
    window.transient(parent)

    frame = ttk.Frame(window, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="WORM Folder Creation", font=("Segoe UI", 14, "bold")).pack(pady=(0, 10))
    ttk.Label(
        frame,
        text="Add input controls and business logic in:\ndocumentation/worm_folder_creation.py",
        justify="center",
    ).pack(pady=5)
    ttk.Button(
        frame,
        text="Run",
        command=lambda: run_gui_action("WORM Folder Creation", execute_worm_folder_creation),
    ).pack(pady=12)
