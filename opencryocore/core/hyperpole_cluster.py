# File: /opencryocore/core/hyperpole_cluster.py

from typing import List
from opencryocore.hardware.structure_shell import StructureShell
from opencryocore.hardware.fan_emitter import FanEmitter
from opencryocore.hardware.piston_generator import PistonGenerator

class HyperPoleUnit:
    """
    Represents a single HyperPole cooling unit.
    Combines metallic shell, fan emitter, and piston generator for hybrid cooling and power harvesting.
    """

    def __init__(self, unit_id: str):
        self.unit_id = unit_id
        self.shell = StructureShell()
        self.fan_emitter = FanEmitter()
        self.piston_generator = PistonGenerator()
        self.operational = False

    def activate(self):
        print(f"[HyperPoleUnit-{self.unit_id}] Activating.")
        self.shell  # Structural setup, no active method needed
        self.fan_emitter.activate(duration_sec=10)
        self.piston_generator.activate()
        self.operational = True

    def shutdown(self):
        print(f"[HyperPoleUnit-{self.unit_id}] Shutting down.")
        self.fan_emitter.shutdown()
        self.piston_generator.shutdown()
        self.operational = False

    def get_status(self):
        return {
            "unit_id": self.unit_id,
            "operational": self.operational,
            "fan_status": self.fan_emitter.get_status(),
            "power_output": self.piston_generator.get_current_output()
        }


class HyperPoleCluster:
    """
    Manages a cluster of HyperPoleUnits.
    Coordinates activation, power management, and cooling distribution.
    """

    def __init__(self, cluster_id: str, power_budget_watts: float, unit_count: int = 9):
        self.cluster_id = cluster_id
        self.power_budget_watts = power_budget_watts
        self.units: List[HyperPoleUnit] = [HyperPoleUnit(f"{cluster_id}_unit_{i+1}") for i in range(unit_count)]
        self.operational = False

    def activate_cluster(self):
        print(f"[HyperPoleCluster-{self.cluster_id}] Activating cluster with {len(self.units)} units.")
        for unit in self.units:
            unit.activate()
        self.operational = True

    def shutdown_cluster(self):
        print(f"[HyperPoleCluster-{self.cluster_id}] Shutting down cluster.")
        for unit in self.units:
            unit.shutdown()
        self.operational = False

    def run_cooling_cycle(self, duration_seconds: int):
        """
        Simulate cooling output cycle for all units.
        """
        if not self.operational:
            print(f"[HyperPoleCluster-{self.cluster_id}] Cluster not operational.")
            return

        print(f"[HyperPoleCluster-{self.cluster_id}] Running cooling cycle for {duration_seconds} seconds.")
        for unit in self.units:
            # Simulate piston generator impacts randomly
            unit.piston_generator.simulate_impact(force_level=0.8)
            unit.fan_emitter.activate(duration_sec=duration_seconds)

    def cluster_status(self):
        return {
            "cluster_id": self.cluster_id,
            "operational": self.operational,
            "unit_count": len(self.units),
            "units_status": [unit.get_status() for unit in self.units]
        }
