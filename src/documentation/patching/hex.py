"""HEX patching GUI placeholder and extension point."""
from __future__ import annotations
import logging
import tkinter as tk
from tkinter import ttk
from app_common import not_implemented, run_gui_action
LOGGER = logging.getLogger(__name__)


def execute_hex_patching() -> None:
    """Implement HEX patching logic here."""
    not_implemented("HEX Patching")


def open_hex(parent: tk.Misc) -> None:
    LOGGER.debug("Opening HEX patching dialog")
    window = tk.Toplevel(parent)
    window.title("HEX Patching")
    window.geometry("390x180")
    window.transient(parent)
    frame = ttk.Frame(window, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="HEX Patching", font=("Segoe UI", 14, "bold")).pack(pady=8)
    ttk.Label(frame, text="Add inputs and patching logic in this module.").pack(pady=5)
    ttk.Button(frame, text="Run", command=lambda: run_gui_action("HEX Patching", execute_hex_patching)).pack(pady=12)
