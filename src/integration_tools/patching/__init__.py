"""Patching GUI that links A2L, CPS, HEX, and CFA patch modules."""

from __future__ import annotations
import tkinter as tk
from tkinter import ttk

from integration_tools.patching.a2l import open_a2l
from integration_tools.patching.cps import open_cps
from integration_tools.patching.hex import open_hex
from integration_tools.patching.cfa import open_cfa


def open_patching(parent: tk.Misc) -> None:
    window = tk.Toplevel(parent)
    window.title("Patching")
    window.geometry("280x250")
    window.transient(parent)
    window.resizable(False, False)

    frame = ttk.Frame(window, padding=15)
    frame.pack(fill="both", expand=True)

    ttk.Label(
        frame,
        text="Patching",
        font=("Segoe UI", 12, "bold")
    ).pack(pady=(0, 10))

    # Checkbox variables
    a2l_var = tk.BooleanVar()
    cps_var = tk.BooleanVar()
    hex_var = tk.BooleanVar()
    cfa_var = tk.BooleanVar()
    all_var = tk.BooleanVar()

    def select_all():
        state = all_var.get()
        a2l_var.set(state)
        cps_var.set(state)
        hex_var.set(state)
        cfa_var.set(state)

    ttk.Checkbutton(
        frame,
        text="Select All",
        variable=all_var,
        command=select_all
    ).pack(anchor="w", pady=(0, 5))

    ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=5)

    ttk.Checkbutton(frame, text="A2L", variable=a2l_var).pack(anchor="w", pady=3)
    ttk.Checkbutton(frame, text="CPS", variable=cps_var).pack(anchor="w", pady=3)
    ttk.Checkbutton(frame, text="HEX", variable=hex_var).pack(anchor="w", pady=3)
    ttk.Checkbutton(frame, text="CFA", variable=cfa_var).pack(anchor="w", pady=3)

    def run_patch():
        if a2l_var.get():
            open_a2l(window)

        if cps_var.get():
            open_cps(window)

        if hex_var.get():
            open_hex(window)

        if cfa_var.get():
            open_cfa(window)

    ttk.Button(
        frame,
        text="Patch",
        command=run_patch
    ).pack(fill="x", pady=(15, 0), ipady=5)