from __future__ import annotations
import logging
import tkinter as tk
from app_common import not_implemented, run_gui_action

LOGGER = logging.getLogger(__name__)


def execute_view_creation(self) -> None:
    """Implement Beyond Compare logic here."""

    not_implemented("Beyond Compare")
    self.set_status("READY")


def beyond_compare(self, parent: tk.Misc):
    mode = self.compare_file.get()
    self.set_status("Running: Beyond Compare: " + mode)
    LOGGER.debug("Beyond Compare requested (%s)", mode)
    execute_view_creation(self)