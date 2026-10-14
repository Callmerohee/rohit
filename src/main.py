"""EasyTool compact Tkinter GUI entry point."""
from __future__ import annotations

import logging
import tkinter as tk
from tkinter import ttk

from app_common import configure_logging
from buildproject.load_releaseinfo import load_release_info
from buildproject.build_project import build_project
from buildproject.beyond_compare import beyond_compare
from buildproject.view_creation import open_view_creation
from buildproject.update_configuration import edit_configspec
from buildproject.update_project_config import update_project_config
from buildproject.label_update import open_label_update
from integration_tools.ADOKU import open_ADOKU_creation
from integration_tools.copy_to_release import open_copy_to_release
from integration_tools.diagdb_creation import open_diagdb_creation
from integration_tools.resource_generation import open_resource_generation
from integration_tools.patching import open_patching
from integration_tools.worm.worm_folder_creation import open_worm_folder_creation
from integration_tools.worm.check_format import open_check_format
from integration_tools.worm.deliver_to_worm import open_deliver_to_worm

LOGGER = logging.getLogger(__name__)


class EasyToolApp(tk.Tk):
    """Main application window linking all feature modules."""

    def __init__(self) -> None:
        super().__init__()
        self.title("EasyTool")
        self.geometry("920x290")
        self.minsize(820, 290)
        self.protocol("WM_DELETE_WINDOW", self._close)
        # -----------------------------------------------------
        # APPLICATION VARIABLES
        # -----------------------------------------------------
        self.label_source = tk.StringVar(value="CQ")
        self.compare_file = tk.StringVar(value="Configspec")

        self.view_name = tk.StringVar(value="-")
        self.drive_letter = tk.StringVar(value="V:")
        self.chk_patching = tk.BooleanVar()
        self.chk_diagdb = tk.BooleanVar()
        self.chk_resource = tk.BooleanVar()
        self.chk_copy_release = tk.BooleanVar()

        self.cpu_load = tk.StringVar()



        self.progress_value = tk.DoubleVar(value=0)
        self.progress_text = tk.StringVar(value="0%")

        self.status_text = tk.StringVar(value="READY")

        self.configure(bg="#d3d6da")

        self._configure_style()
        self._build_ui()

        LOGGER.info("EasyTool GUI initialized")


    # =========================================================
    # STYLE
    # =========================================================
    def _configure_style(self):
        style = ttk.Style(self)

        available_themes = style.theme_names()

        if "vista" in available_themes:
            style.theme_use("default")
        elif "clam" in available_themes:
            style.theme_use("clam")

        default_font = ("Segoe UI", 9)
        heading_font = ("Segoe UI", 9, "bold")

        style.configure(
            ".",
            font=default_font
        )

        style.configure(
            "Main.TFrame",
            background="#d3d6da"
        )

        style.configure(
            "Panel.TLabelframe",
            background="#d3d6da",
            borderwidth=1,
            relief="groove",
            padding=7
        )

        style.configure(
            "Panel.TLabelframe.Label",
            background="#d3d6da",
            foreground="#111111",
            font=heading_font
        )

        style.configure(
            "Section.TLabel",
            background="#d3d6da",
            foreground="#111111",
            font=heading_font
        )

        style.configure(
            "Field.TLabel",
            background="#d3d6da",
            foreground="#111111"
        )

        style.configure(
            "Tool.TButton",
            font=default_font,
            padding=(10, 5)
        )

        style.configure(
            "Tool.TCheckbutton",
            background="#d3d6da"
        )

        style.configure(
            "Tool.TRadiobutton",
            background="#d3d6da"
        )

        style.configure(
            "Tool.Horizontal.TProgressbar",
            thickness=17
        )

        style.map(
            "Tool.TButton",
            relief=[
                ("pressed", "sunken"),
                ("active", "raised")
            ]
        )

    # =========================================================
    # MAIN LAYOUT
    # =========================================================
    def _build_ui(self):
        main = ttk.Frame(
            self,
            style="Main.TFrame",
            padding=7
        )
        main.pack(fill="both", expand=True)

        main.columnconfigure(0, weight=1, uniform="main")
        main.columnconfigure(1, weight=1, uniform="main")

        main.rowconfigure(0, weight=0)
        main.rowconfigure(1, weight=0)
        main.rowconfigure(2, weight=0)

        left_panel = ttk.Frame(
            main,
            style="Main.TFrame"
        )
        left_panel.grid(
            row=0,
            column=0,
            rowspan=2,
            sticky="nsew",
            padx=(0, 4)
        )

        right_panel = ttk.Frame(
            main,
            style="Main.TFrame"
        )
        right_panel.grid(
            row=0,
            column=1,
            rowspan=2,
            sticky="nsew",
            padx=(4, 0)
        )

        left_panel.columnconfigure(0, weight=1)
        right_panel.columnconfigure(0, weight=1)

        self._build_project_panel(left_panel)

        self._build_view_panel(left_panel)

        self._build_integration_panel(right_panel)
        self._build_cpu_panel(right_panel)
        self._build_bottom_status_bar()

    # =========================================================
    # BUILD PROJECT PANEL
    # =========================================================
    def _build_project_panel(self, parent):
        frame = ttk.LabelFrame(
            parent,
            text="Build Project",
            style="Panel.TLabelframe"
        )
        frame.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, 7)
        )

        for column in range(3):
            frame.columnconfigure(
                column,
                weight=1,
                uniform="build-buttons"
            )
        self.PAD_X = 3
        self.PAD_Y = 3
        ttk.Button(
            frame,
            text="Load Release Info",
            style="Tool.TButton",
            command=lambda: load_release_info(self,parent)
        ).grid(
            row=0,
            column=0,
            sticky="ew",
            padx=self.PAD_X,
            pady=self.PAD_Y
        )

        ttk.Button(
            frame,
            text="Create View",
            style="Tool.TButton",
            command=lambda: open_view_creation(self,parent)
        ).grid(
            row=0,
            column=1,
            sticky="ew",
            padx=self.PAD_X,
            pady=self.PAD_Y
        )
        ttk.Button(
            frame,
            text="Edit Configspec",
            style="Tool.TButton",
            command=lambda: edit_configspec(self,parent)
        ).grid(
            row=0,
            column=2,
            sticky="ew",
            padx=self.PAD_X,
            pady=self.PAD_Y
        )
        ttk.Button(
            frame,
            text="Projectconfig.mak",
            style="Tool.TButton",
            command=lambda: update_project_config(self,parent)
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=self.PAD_X,
            pady=self.PAD_Y
        )

        ttk.Button(
            frame,
            text="Load Labels",
            style="Tool.TButton",
            command=lambda: open_label_update(self,parent)
        ).grid(
            row=1,
            column=1,
            sticky="ew",
            padx=self.PAD_X,
            pady=self.PAD_Y
        )

        ttk.Combobox(
            frame,
            textvariable=self.label_source,
            values=["CQ", "Manual"],
            state="readonly",
            width=12
        ).grid(
            row=1,
            column=2,
            sticky="ew",
            padx=self.PAD_X,
            pady=self.PAD_Y
        )

        ttk.Button(
            frame,
            text="Build Project",
            style="Tool.TButton",
            command=lambda: build_project(self)
        ).grid(
            row=2,
            column=0,
            sticky="ew",
            padx=self.PAD_X,
            pady=self.PAD_Y
        )

        ttk.Button(
            frame,
            text="Beyond Compare",
            style="Tool.TButton",
            command=lambda: beyond_compare(self,parent)
        ).grid(
            row=2,
            column=1,
            sticky="ew",
            padx=self.PAD_X,
            pady=self.PAD_Y
        )

        ttk.Combobox(
            frame,
            textvariable=self.compare_file,
            values=["Configspec", "Projectconfig.mak"],
            state="readonly",
            width=18
        ).grid(
            row=2,
            column=2,
            sticky="ew",
            padx=(2, 3)
        )





    # =========================================================
    # VIEW PANEL
    # =========================================================
    def _build_view_panel(self, parent):
        frame = ttk.LabelFrame(
            parent,
            text="View Information",
            style="Panel.TLabelframe"
        )
        frame.grid(
            row=2,
            column=0,
            sticky="nsew"
        )

        frame.columnconfigure(1, weight=1)

        ttk.Label(
            frame,
            text="View:",
            style="Field.TLabel"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 5)
        )

        view_entry = ttk.Entry(
            frame,
            textvariable=self.view_name,
            state="readonly",
            font=("Segoe UI", 9)
        )
        view_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=(0, 5)
        )

        self.drive_combo = ttk.Combobox(
            frame,
            textvariable=self.drive_letter,
            values=["V:", "W:", "X:", "Y:", "Z:"],
            width=4,
            state="readonly"
        )
        self.drive_combo.grid(
            row=0,
            column=2,
            sticky="e"
        )

        progress_row = ttk.Frame(frame)
        progress_row.grid(
            row=1,
            column=0,
            columnspan=3,
            sticky="ew",
            pady=(10, 0)
        )

        progress_row.columnconfigure(0, weight=1)

        self.progress = ttk.Progressbar(
            progress_row,
            maximum=100,
            variable=self.progress_value,
            style="Tool.Horizontal.TProgressbar"
        )
        self.progress.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        ttk.Label(
            progress_row,
            textvariable=self.progress_text,
            width=5
        ).grid(
            row=0,
            column=1,
            padx=(5, 0)
        )

    # =========================================================
    # INTEGRATION PANEL
    # =========================================================
    def _build_integration_panel(self, parent):
        frame = ttk.LabelFrame(
            parent,
            text="Integration Tools",
            style="Panel.TLabelframe"
        )
        frame.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, 7)
        )

        for column in range(2):
            frame.columnconfigure(
                column,
                weight=1,
                uniform="buildproject-buttons"
            )

        buttons = [
            ("ADOKU", lambda: open_ADOKU_creation(self, parent)),
            ("Patching", lambda: open_patching(self, parent)),
            ("DiagDB", lambda: open_diagdb_creation(self, parent)),
            ("Resource Generation", lambda: open_resource_generation(self, parent)),
            ("Copy To Release", lambda: open_copy_to_release(self, parent)),
            ("WORM", lambda: open_worm_folder_creation(self, parent)),
            ("Check WORM", lambda: open_check_format(self, parent)),
            ("Deliver WORM", lambda: open_deliver_to_worm(self, parent))
        ]

        for index, (text, command) in enumerate(buttons):
            row = index // 3
            column = index % 3

            left_padding = 0 if column == 0 else 4
            right_padding = 4 if column == 0 else 0

            ttk.Button(
                frame,
                text=text,
                style="Tool.TButton",
                command=command
            ).grid(
                row=row,
                column=column,
                sticky="ew",
                padx=self.PAD_X,
                pady=self.PAD_Y
            )
        # --------------------------------------------------
        # OPTION CHECKBOXES
        # --------------------------------------------------

        check_frame = ttk.Frame(
            frame,
            style="Main.TFrame"
        )

        check_frame.grid(
            row=3,
            column=0,
            columnspan=3,
            sticky="w",
            pady=(12, 8)
        )

        ttk.Checkbutton(
            check_frame,
            text="Patching",
            variable=self.chk_patching
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 20)
        )

        ttk.Checkbutton(
            check_frame,
            text="DiagDB",
            variable=self.chk_diagdb
        ).grid(
            row=0,
            column=1,
            sticky="w",
            padx=(0, 20)
        )


        ttk.Checkbutton(
            check_frame,
            text="Resource Generation",
            variable=self.chk_resource
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=(0, 20)
        )

        ttk.Checkbutton(
            check_frame,
            text="Copy To Release",
            variable=self.chk_copy_release
        ).grid(
            row=0,
            column=3,
            sticky="w",
            padx=(0, 20)
        )
    # =========================================================
    # CPU PANEL
    # =========================================================
    def _build_cpu_panel(self, parent):
        frame = ttk.LabelFrame(
            parent,
            text="CPU Load",
            style="Panel.TLabelframe"
        )
        frame.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        frame.columnconfigure(1, weight=1)

        ttk.Label(
            frame,
            text="CPU Load:",
            style="Field.TLabel"
        ).grid(
            row=0,
            column=0,
            sticky="e",
            padx=(0, 8),
            pady=(0, 7)
        )

        cpu_entry = ttk.Entry(
            frame,
            textvariable=self.cpu_load
        )
        cpu_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            pady=(0, 7)
        )


    # =========================================================
    # BOTTOM STATUS BAR
    # =========================================================
    def _build_bottom_status_bar(self):
        status_bar = tk.Frame(
            self,
            bg="#c4c7cb",
            relief="sunken",
            borderwidth=1
        )
        status_bar.pack(
            side="bottom",
            fill="x"
        )

        tk.Label(
            status_bar,
            text="EasyTool",
            bg="#c4c7cb",
            fg="#222222",
            anchor="w",
            padx=7,
            pady=2
        ).pack(
            side="left",
            fill="x",
            expand=True
        )

        tk.Label(
            status_bar,
            textvariable=self.status_text,
            bg="#c4c7cb",
            fg="#222222",
            anchor="e",
            padx=7,
            pady=2
        ).pack(side="right")

    # =========================================================
    # HELPERS
    # =========================================================

    def set_progress(self, value):
        value = max(0, min(100, value))

        self.progress_value.set(value)
        self.progress_text.set(f"{int(value)}%")

    def set_status(self, text, color=None):
        self.status_text.set(text)

        if hasattr(self, "status_indicator"):
            try:
                self.status_indicator.configure(bg=color)
            except:
                pass

        self.update_idletasks()



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
