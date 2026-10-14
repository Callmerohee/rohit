"""Deliver to WORM GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_deliver_to_worm() -> None:
    """Implement the Deliver to WORM business logic here."""
    not_implemented("Deliver to WORM")


def open_deliver_to_worm(self, parent: tk.Misc) -> None:
    """Open the Deliver to WORM dialog."""
    LOGGER.debug("Opening Deliver to WORM dialog")
    self.set_status("Running: Deliver to WORM")
    execute_deliver_to_worm()
    self.set_status("READY")