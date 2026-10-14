"""Optional buildproject view creation extension point."""
from __future__ import annotations
import logging
import tkinter as tk
from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_view_creation(self) -> None:
    """Implement buildproject view creation logic here."""

    not_implemented("View Creation")
    self.set_status("READY")

def open_view_creation(self, parent: tk.Misc) -> None:
    """Run the view creation placeholder from another GUI when needed."""
    self.set_status("Running: View Creation")
    LOGGER.debug("View Creation requested")
    execute_view_creation(self)
