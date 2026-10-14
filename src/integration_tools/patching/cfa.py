"""CFA patching GUI placeholder and extension point."""
from __future__ import annotations
import logging
import tkinter as tk
from tkinter import ttk
from app_common import not_implemented, run_gui_action
LOGGER = logging.getLogger(__name__)


def execute_cfa_patching() -> None:
    """Implement CFA patching logic here."""
    not_implemented("CFA Patching")


def open_cfa(self, parent: tk.Misc) -> None:
    LOGGER.debug("Opening CFA patching dialog")
    self.set_status("Running: CFA Patching")
    execute_cfa_patching()
    self.set_status("READY")
