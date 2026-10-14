"""Resource Generation GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_resource_generation(self) -> None:
    """Implement the Resource Generation business logic here."""
    not_implemented("Resource Generation")


def open_resource_generation(self, parent: tk.Misc) -> None:
    """Open the Resource Generation dialog."""
    LOGGER.debug("Opening Resource Generation dialog")
    self.set_status("Running: Resource Generation")
    execute_resource_generation(self)
    self.set_status("READY")
