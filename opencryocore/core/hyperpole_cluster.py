# File: /opencryocore/core/hyperpole_cluster.py

from typing import List
from .cryocore_unit import CryoCoreUnit
import time

class HyperPoleCluster:
    """
    Manages a 9-unit CryoCore cluster acting as a unified HyperPole cooling tower.
    Each unit operates in sync to maximize radial cooling and vertical convection.
    """

    def __init__(self, cluster_id: str, power_budget_watts: float, ambient_temp_c: float = 45.0):
        """
        Initialize a HyperPoleCluster with 9 CryoCore units.
        :param cluster_id: Unique cluster identifier
        :param power_budget_watts: Total available power for all 9 cores
        :param ambient_temp_c: External starting temperature
        """
        self.cluster_id = cluster_id
        self.power_budget_watts = power_budget_watts
        self.ambient_temp_c = ambient_temp_c
        self.units: List[CryoCoreUnit] = []
        self.operational = False

        self._initialize_units()

    def _initialize_units(self):
        unit_power = self.power_budget_watts / 9.0
        for i in range(9):
            unit_id = f"{self.cluster_id}_core{i+1}"
            unit = CryoCoreUnit(unit_id, unit_power, self.ambient_temp_c)
            self.units.append(unit)

    def activate_cluster(self):
        print(f"[{self.cluster_id}] Activating HyperPole cluster...")
        for unit in self.units:
            unit.startup_sequence()
        self.operational = all(unit.operational for unit in self.units)
        if self.operational:
            print(f"[{self.cluster_id}] Cluster fully operational.")
        else:
            print(f"[{self.cluster_id}] Cluster failed to activate all units.")

    def run_cooling_cycle(self, duration_seconds: int = 60):
        """
        Activate simultaneous cooling cycle on all 9 CryoCore units.
        """
        if not self.operational:
            print(f"[{self.cluster_id}] Cluster not operational. Cannot cool.")
            return

        print(f"[{self.cluster_id}] Running coordinated cooling cycle...")
        for unit in self.units:
            unit.cool_environment(seconds=duration_seconds)

    def shutdown_cluster(self):
        print(f"[{self.cluster_id}] Shutting down cluster...")
        for unit in self.units:
            unit.shutdown_sequence()
        self.operational = False

    def cluster_status(self) -> dict:
        return {
            "cluster_id": self.cluster_id,
            "operational": self.operational,
            "ambient_temp_c": self.ambient_temp_c,
            "unit_statuses": [unit.status() for unit in self.units]
        }
