# File: /opencryocore/control/core_controller.py

import time
from opencryocore.hardware.power_interface import PowerInterface, PowerSourceType
from opencryocore.hardware.sensor_array import SensorArray
from opencryocore.core.hyperpole_cluster import HyperPoleCluster
from opencryocore.core.environment_sim import EnvironmentSim
from opencryocore.display.oled_driver import OLEDStatusDisplay

class CryoCoreController:
    """
    Central controller for a full CryoCore HyperPole system.
    Ties together sensors, cooling engine, environment model, and display interface.
    """

    def __init__(self, cluster_id: str = "core01"):
        self.cluster_id = cluster_id

        # Initialize subsystems
        self.power = PowerInterface(source_type=PowerSourceType.SOLAR, max_output_watts=135.0)
        self.sensors = SensorArray()
        self.environment = EnvironmentSim(initial_temp_c=45.0, radius_ft=9.0, height_ft=20.0)
        self.cluster = HyperPoleCluster(cluster_id, power_budget_watts=135.0)
        self.display = OLEDStatusDisplay(get_status_callback=self.get_status)

        self.running = False

    def initialize(self):
        print(f"[{self.cluster_id}] Initializing CryoCore controller...")
        self.power.activate()
        self.cluster.activate_cluster()

    def run_loop(self, cycle_seconds: int = 60):
        self.running = True
        print(f"[{self.cluster_id}] Starting control loop.")

        while self.running:
            sensor_data = self.sensors.read_environment()
            solar_watts = self.power.get_current_output(time_of_day=12.0)

            # Apply cooling based on available power
            self.environment.apply_cooling(cooling_watts=solar_watts, seconds=cycle_seconds)
            self.cluster.run_cooling_cycle(duration_seconds=cycle_seconds)

            # Update OLED display
            self.display.update_display()

            # Print simulated environment
            env = self.environment.report()
            print(f"[{self.cluster_id}] Ambient Temp: {env['current_temp_c']:.2f}°C | "
                  f"Air Volume: {env['air_volume_m3']} m³")

            # Passive reheat simulation
            self.environment.recover_heat(seconds=cycle_seconds)

            time.sleep(cycle_seconds)

    def shutdown(self):
        print(f"[{self.cluster_id}] Shutting down controller.")
        self.cluster.shutdown_cluster()
        self.power.shutdown()
        self.running = False

    def get_status(self):
        """
        Returns live status for OLED/UI display.
        """
        cluster_stat = self.cluster.cluster_status()
        env = self.environment.report()
        return {
            "cluster_id": cluster_stat["cluster_id"],
            "operational": cluster_stat["operational"],
            "ambient_temp_c": env["current_temp_c"]
        }
