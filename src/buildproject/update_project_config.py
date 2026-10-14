"""Update Project Config GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_update_project_config(self) -> None:
    """Implement the Update Project Config business logic here."""
    not_implemented("Update Project Config")
    self.set_status("READY")

def update_project_config(self,parent: tk.Misc) -> None:
    """Open the Update Project Config dialog."""
    LOGGER.debug("Opening Update Project Config dialog")
    self.set_status("Running: Update Project Config")
    execute_update_project_config(self)