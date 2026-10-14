"""ADOKU folder creation GUI placeholder and extension point."""
from __future__ import annotations

import logging
import tkinter as tk
from integration_tools.resource_generation import open_resource_generation
from integration_tools.copy_to_release import open_copy_to_release
from integration_tools.diagdb_creation import open_diagdb_creation
from integration_tools.patching import open_patching
LOGGER = logging.getLogger(__name__)


def execute_ADOKU_workflow(self, parent) -> None:
    """Implement the ADOKU folder creation business logic here."""
    LOGGER.debug("ADOKU workflow execution started with selected options.")
    self.set_status("Running: ADOKU Workflow")
    if self.chk_patching.get():
        open_patching(self, parent)

    if self.chk_diagdb.get():
        open_diagdb_creation(self, parent)

    if self.chk_resource.get():
        open_resource_generation(self, parent)

    if self.chk_copy_release.get():
        open_copy_to_release(self, parent)

def create_ADOKU(self, parent):
    LOGGER.debug("Opening ADOKU Creation dialog")
    self.set_status("Running: ADOKU Creation")


def open_ADOKU_creation(self, parent: tk.Misc) -> None:
    """Open the ADOKU Creation dialog."""
    create_ADOKU(self, parent)
    execute_ADOKU_workflow(self, parent)
    self.set_status("READY")
