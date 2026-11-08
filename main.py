"""Bloomie - virtuaalne õppeaed, mis kasvab ülesannete täitmisel.

Autorid: Varvara Gavrilova ja Elmira Rafiyeva
Allikad: Pythoni dokumentatsioon (tkinter, json, pathlib).
"""

import json
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

def laadi_andmed():
    if not ANDMEFAIL.exists():
        return []