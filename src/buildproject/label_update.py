"""Label Update GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_label_update(self) -> None:
    """Implement the Label Update business logic here."""
    not_implemented("Label Update")
    self.set_status("READY")

def open_label_update(self,parent: tk.Misc) -> None:
    """Open the Label Update dialog."""
    mode = self.label_source.get()
    LOGGER.debug("Opening Label Update(%s) dialog", mode)
    self.set_status("Running: Label Update" + f" ({mode})")
    execute_label_update(self)