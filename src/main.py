"""EasyTool compact Tkinter GUI entry point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import configure_logging
from integration.update_configuration import open_update_configuration
from integration.update_project_config import open_update_project_config
from integration.label_update import open_label_update
from documentation.work_folder_creation import open_work_folder_creation
from documentation.copy_to_release import open_copy_to_release
from documentation.diagdb_creation import open_diagdb_creation
from documentation.resource_generation import open_resource_generation
from documentation.worm_folder_creation import open_worm_folder_creation
from documentation.patching import open_patching
from documentation.worm.check_format import open_check_format
from documentation.worm.deliver_to_worm import open_deliver_to_worm

LOGGER = logging.getLogger(__name__)

BUTTONS = (
    ("Update Configuration", open_update_configuration),
    ("Update Project Config", open_update_project_config),
    ("Label Update", open_label_update),
    ("Work Folder Creation", open_work_folder_creation),
    ("Copy to Release", open_copy_to_release),
    ("DiagDB Creation", open_diagdb_creation),
    ("Resource Generation", open_resource_generation),
    ("WORM Folder Creation", open_worm_folder_creation),
    ("Patching", open_patching),
    ("Check Format", open_check_format),
    ("Deliver to WORM", open_deliver_to_worm),
)


class EasyToolApp(tk.Tk):
    """Main application window linking all feature modules."""

    def __init__(self) -> None:
        super().__init__()
        self.title("EasyTool")
        self.geometry("520x570")
        self.minsize(460, 500)
        self.protocol("WM_DELETE_WINDOW", self._close)
        self._build_ui()
        LOGGER.info("EasyTool GUI initialized")

    def _build_ui(self) -> None:
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="EasyTool", font=("Segoe UI", 20, "bold")).pack(pady=(0, 5))
        ttk.Label(frame, text="Select an operation").pack(pady=(0, 15))

        button_frame = ttk.Frame(frame)
        button_frame.pack(fill="both", expand=True)
        for index, (label, callback) in enumerate(BUTTONS):
            row, column = divmod(index, 2)
            button = ttk.Button(button_frame, text=label, command=lambda cb=callback: cb(self))
            button.grid(row=row, column=column, sticky="nsew", padx=6, pady=6, ipady=9)
        for column in range(2):
            button_frame.columnconfigure(column, weight=1)
        for row in range(6):
            button_frame.rowconfigure(row, weight=1)

        ttk.Label(frame, text="Detailed events are stored in log/Log.txt").pack(pady=(12, 0))

    def _close(self) -> None:
        LOGGER.info("EasyTool GUI closed")
        self.destroy()


def main() -> int:
    configure_logging()
    try:
        app = EasyToolApp()
        app.mainloop()
        return 0
    except KeyboardInterrupt:
        LOGGER.warning("Application interrupted by user")
        return 130
    except Exception:
        LOGGER.exception("Fatal application error")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
