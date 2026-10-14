"""Copy to Release GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_copy_to_release(self) -> None:
    """Implement the Copy to Release business logic here."""
    not_implemented("Copy to Release")


def open_copy_to_release(self, parent: tk.Misc) -> None:
    """Open the Copy to Release dialog."""
    LOGGER.debug("Opening Copy to Release dialog")
    self.set_status("Running: Copy to Release")
    execute_copy_to_release(self)
    self.set_status("READY")
