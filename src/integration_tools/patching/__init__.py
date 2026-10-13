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
    window.geometry("350x300")
    window.transient(parent)
    frame = ttk.Frame(window, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Patching", font=("Segoe UI", 14, "bold")).pack(pady=(0, 12))
    for label, callback in (("A2L", open_a2l), ("CPS", open_cps), ("HEX", open_hex), ("CFA", open_cfa)):
        ttk.Button(frame, text=label, command=lambda cb=callback: cb(window)).pack(fill="x", pady=5, ipady=5)
