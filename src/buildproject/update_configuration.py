"""Update Configuration GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_update_configuration() -> None:
    """Implement the Update Configuration business logic here."""
    not_implemented("Update Configuration")


def edit_configspec(parent: tk.Misc) -> None:
    """Open the Update Configuration dialog."""
    LOGGER.debug("Opening Update Configuration dialog")
    window = tk.Toplevel(parent)
    window.title("Update Configuration")
    window.geometry("420x190")
    window.transient(parent)

    frame = ttk.Frame(window, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Update Configuration", font=("Segoe UI", 14, "bold")).pack(pady=(0, 10))
    ttk.Label(
        frame,
        text="Add input controls and business logic in:\nbuildproject/update_configuration.py",
        justify="center",
    ).pack(pady=5)
    ttk.Button(
        frame,
        text="Run",
        command=lambda: run_gui_action("Update Configuration", execute_update_configuration),
    ).pack(pady=12)
