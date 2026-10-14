"""Update Configuration GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_update_configuration(self) -> None:
    """Implement the Update Configuration business logic here."""
    not_implemented("Update Configuration")
    self.set_status("READY")

def edit_configspec(self, parent: tk.Misc) -> None:
    """Open the Update Configuration dialog."""
    LOGGER.debug("Opening Update Configuration dialog")
    self.set_status("Running: Update Configuration")
    execute_update_configuration(self)