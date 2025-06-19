# File: /opencryocore/display/touch_ui.py

import tkinter as tk
from tkinter import ttk
from typing import Optional

class CryoCoreUI:
    """
    A simple touch-friendly GUI using Tkinter for monitoring a CryoCore or HyperPole system.
    Displays status, temperatures, and control buttons for Raspberry Pi with touchscreen.
    """

    def __init__(self, cluster_status_func, shutdown_func, refresh_interval_ms: int = 1000):
        """
        :param cluster_status_func: Callable that returns the current system status as a dict
        :param shutdown_func: Callable to initiate system shutdown
        :param refresh_interval_ms: How often to refresh UI in milliseconds
        """
        self.root = tk.Tk()
        self.cluster_status_func = cluster_status_func
        self.shutdown_func = shutdown_func
        self.refresh_interval_ms = refresh_interval_ms
        self.status_labels = {}

        self.root.title("CryoCore System Monitor")
        self.root.geometry("480x320")  # Typical Raspberry Pi touch resolution
        self.root.configure(bg="#111")

        self._build_ui()
        self._schedule_refresh()

    def _build_ui(self):
        header = tk.Label(self.root, text="CryoCore HyperPole", font=("Arial", 20, "bold"), bg="#111", fg="#0ff")
        header.pack(pady=10)

        self.status_frame = tk.Frame(self.root, bg="#111")
        self.status_frame.pack(pady=5)

        for key in ["cluster_id", "operational", "ambient_temp_c"]:
            label = tk.Label(self.status_frame, text=f"{key}: ---", font=("Arial", 14), bg="#111", fg="#eee")
            label.pack()
            self.status_labels[key] = label

        self.unit_frame = tk.Frame(self.root, bg="#111")
        self.unit_frame.pack(pady=5)

        self.shutdown_button = ttk.Button(self.root, text="Shutdown System", command=self._on_shutdown)
        self.shutdown_button.pack(pady=10)

    def _on_shutdown(self):
        self.shutdown_func()
        for label in self.status_labels.values():
            label.config(text="---")
        print("[UI] Shutdown initiated.")

    def _schedule_refresh(self):
        self._update_status()
        self.root.after(self.refresh_interval_ms, self._schedule_refresh)

    def _update_status(self):
        status = self.cluster_status_func()
        if not status:
            return
        for key in ["cluster_id", "operational", "ambient_temp_c"]:
            value = status.get(key, "---")
            if isinstance(value, float):
                value = f"{value:.2f}"
            self.status_labels[key].config(text=f"{key}: {value}")

    def run(self):
        self.root.mainloop()
