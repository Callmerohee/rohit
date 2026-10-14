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


def open_hex(self, parent: tk.Misc) -> None:
    LOGGER.debug("Opening HEX patching dialog")
    self.set_status("Running: HEX Patching")
    execute_hex_patching()
    self.set_status("READY")
