"""CPS patching GUI placeholder and extension point."""
from __future__ import annotations
import logging
import tkinter as tk
from tkinter import ttk
from app_common import not_implemented, run_gui_action
LOGGER = logging.getLogger(__name__)


def execute_cps_patching() -> None:
    """Implement CPS patching logic here."""
    not_implemented("CPS Patching")


def open_cps(self, parent: tk.Misc) -> None:
    LOGGER.debug("Opening CPS patching dialog")
    self.set_status("Running: CPS Patching")
    execute_cps_patching()
    self.set_status("READY")

