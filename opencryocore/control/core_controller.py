# File: /opencryocore/control/core_controller.py

import time
from opencryocore.core.environment_sim import EnvironmentSim
from opencryocore.core.hyperpole_cluster import HyperPoleCluster
from opencryocore.hardware.power_interface import PowerInterface

class CryoCoreController:
    """
    Main control logic for the CryoCore system.
    Integrates cooling cluster, power management, and environmental simulation.
    """

    def __init__(self, cluster_id: str):
        self.cluster_id = cluster_id
        self.power_interface = PowerInterface()
        self.hyperpole_cluster = HyperPoleCluster(cluster_id=cluster_id, power_budget_watts=360)
        self.environment_sim = EnvironmentSim()
        self.operational = False

    def initialize(self):
        print(f"[CryoCoreController-{self.cluster_id}] Initializing system.")
        self.power_interface.power_on()
        self.hyperpole_cluster.activate_cluster()
        self.operational = True

    def run_loop(self, cycle_seconds: int = 10):
        """
        Runs the main operational loop with power consumption, cooling, and environment updates.
        """
        print(f"[CryoCoreController-{self.cluster_id}] Starting main loop. Cycle time: {cycle_seconds} seconds.")
        try:
            while self.operational:
                # Power consumption for cooling and fans
                power_load_watts = self.hyperpole_cluster.power_budget_watts
                self.power_interface.consume_power(power_load_watts, cycle_seconds / 3600)

                # Run cooling cycle on cluster
                self.hyperpole_cluster.run_cooling_cycle(cycle_seconds)

                # Apply cooling to environment simulation
                self.environment_sim.apply_cooling(power_load_watts, cycle_seconds)

                # Recover ambient heat over the cycle duration
                self.environment_sim.recover_heat(cycle_seconds)

                status = self.get_status()
                print(f"[CryoCoreController] Cycle status: {status}")

                time.sleep(cycle_seconds)
        except KeyboardInterrupt:
            print("[CryoCoreController] Shutdown requested via KeyboardInterrupt.")
            self.shutdown()

    def shutdown(self):
        print(f"[CryoCoreController-{self.cluster_id}] Shutting down system.")
        self.operational = False
        self.hyperpole_cluster.shutdown_cluster()
        self.power_interface.power_off()

    def get_status(self) -> dict:
        return {
            "cluster_id": self.cluster_id,
            "operational": self.operational,
            "battery_status": self.power_interface.get_battery_status(),
            "environment": self.environment_sim.report(),
            "cluster_status": self.hyperpole_cluster.cluster_status()
        }
