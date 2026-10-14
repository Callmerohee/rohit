"""A2L patching GUI placeholder and extension point."""
from __future__ import annotations
import logging
import tkinter as tk
from tkinter import ttk
from app_common import not_implemented, run_gui_action
LOGGER = logging.getLogger(__name__)


def execute_a2l_patching() -> None:
    """Implement A2L patching logic here."""
    not_implemented("A2L Patching")


def open_a2l(self,parent: tk.Misc) -> None:
    LOGGER.debug("Opening A2L patching dialog")
    self.set_status("Running: A2L Patching")
    execute_a2l_patching()
    self.set_status("READY")
