"""Deliver to WORM GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_deliver_to_worm() -> None:
    """Implement the Deliver to WORM business logic here."""
    not_implemented("Deliver to WORM")


def open_deliver_to_worm(parent: tk.Misc) -> None:
    """Open the Deliver to WORM dialog."""
    LOGGER.debug("Opening Deliver to WORM dialog")
    window = tk.Toplevel(parent)
    window.title("Deliver to WORM")
    window.geometry("420x190")
    window.transient(parent)

    frame = ttk.Frame(window, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Deliver to WORM", font=("Segoe UI", 14, "bold")).pack(pady=(0, 10))
    ttk.Label(
        frame,
        text="Add input controls and business logic in:\nintegration_tools/worm/deliver_to_worm.py",
        justify="center",
    ).pack(pady=5)
    ttk.Button(
        frame,
        text="Run",
        command=lambda: run_gui_action("Deliver to WORM", execute_deliver_to_worm),
    ).pack(pady=12)
