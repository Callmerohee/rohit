from __future__ import annotations
import logging
import tkinter as tk
from app_common import not_implemented, run_gui_action
LOGGER = logging.getLogger(__name__)

def execute_view_creation(self) -> None:
    """Implement Load release info logic here."""
    not_implemented("Load release info")
    self.set_status("READY")


def load_release_info(self, parent: tk.Misc):
    self.set_status("Running: Load Release Info")
    LOGGER.debug("Load release info requested")
    execute_view_creation(self)