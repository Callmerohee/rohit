"""Resource Generation GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_resource_generation() -> None:
    """Implement the Resource Generation business logic here."""
    not_implemented("Resource Generation")


def open_resource_generation(parent: tk.Misc) -> None:
    """Open the Resource Generation dialog."""
    LOGGER.debug("Opening Resource Generation dialog")
    window = tk.Toplevel(parent)
    window.title("Resource Generation")
    window.geometry("420x190")
    window.transient(parent)

    frame = ttk.Frame(window, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Resource Generation", font=("Segoe UI", 14, "bold")).pack(pady=(0, 10))
    ttk.Label(
        frame,
        text="Add input controls and business logic in:\ndocumentation/resource_generation.py",
        justify="center",
    ).pack(pady=5)
    ttk.Button(
        frame,
        text="Run",
        command=lambda: run_gui_action("Resource Generation", execute_resource_generation),
    ).pack(pady=12)
