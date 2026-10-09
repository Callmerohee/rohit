"""Update Project Config GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_update_project_config() -> None:
    """Implement the Update Project Config business logic here."""
    not_implemented("Update Project Config")


def open_update_project_config(parent: tk.Misc) -> None:
    """Open the Update Project Config dialog."""
    LOGGER.debug("Opening Update Project Config dialog")
    window = tk.Toplevel(parent)
    window.title("Update Project Config")
    window.geometry("420x190")
    window.transient(parent)

    frame = ttk.Frame(window, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Update Project Config", font=("Segoe UI", 14, "bold")).pack(pady=(0, 10))
    ttk.Label(
        frame,
        text="Add input controls and business logic in:\nintegration/update_project_config.py",
        justify="center",
    ).pack(pady=5)
    ttk.Button(
        frame,
        text="Run",
        command=lambda: run_gui_action("Update Project Config", execute_update_project_config),
    ).pack(pady=12)
