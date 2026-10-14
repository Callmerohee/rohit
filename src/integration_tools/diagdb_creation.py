"""DiagDB Creation GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_diagdb_creation(self) -> None:
    """Implement the DiagDB Creation business logic here."""
    not_implemented("DiagDB Creation")


def open_diagdb_creation(self, parent: tk.Misc) -> None:
    """Open the DiagDB Creation dialog."""
    LOGGER.debug("Opening DiagDB Creation dialog")
    self.set_status("Running: DiagDB Creation")
    execute_diagdb_creation(self)
    self.set_status("READY")
# Create a new top-level window for the DiagDB Creation dialog