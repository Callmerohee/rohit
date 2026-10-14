"""WORM Folder Creation GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_worm_folder_creation() -> None:
    """Implement the WORM Folder Creation business logic here."""
    not_implemented("WORM Folder Creation")


def open_worm_folder_creation(self, parent: tk.Misc) -> None:
    """Open the WORM Folder Creation dialog."""
    LOGGER.debug("Opening WORM Folder Creation dialog")
    self.set_status("Running: WORM Folder Creation")
    execute_worm_folder_creation()
    self.set_status("READY")