from __future__ import annotations
import logging
import tkinter as tk
from app_common import not_implemented, run_gui_action
LOGGER = logging.getLogger(__name__)

def execute_view_creation(self) -> None:
    """Implement buildproject  logic here."""

    not_implemented("Build Project")
    self.set_status("READY")


def build_project(self):
    self.set_status("Running: Build Project")
    LOGGER.debug("Build project requested")
    execute_view_creation(self)
