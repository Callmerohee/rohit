"""Check Format GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_check_format() -> None:
    """Implement the Check Format business logic here."""
    not_implemented("Check Format")


def open_check_format(self, parent: tk.Misc) -> None:
    """Open the Check Format dialog."""
    LOGGER.debug("Opening Check Format dialog")
    self.set_status("Running: Check Format")
    execute_check_format()
    self.set_status("READY")
