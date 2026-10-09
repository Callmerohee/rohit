"""Optional integration view creation extension point."""
from __future__ import annotations
import logging
import tkinter as tk
from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_view_creation() -> None:
    """Implement integration view creation logic here."""
    not_implemented("View Creation")


def open_view_creation(parent: tk.Misc) -> None:
    """Run the view creation placeholder from another GUI when needed."""
    LOGGER.debug("View Creation requested")
    run_gui_action("View Creation", execute_view_creation)
