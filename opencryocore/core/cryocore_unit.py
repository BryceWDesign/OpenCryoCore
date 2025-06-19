# File: /opencryocore/core/cryocore_unit.py

import time
import math

class CryoCoreUnit:
    """
    CryoCore thermoelectric engine unit.
    Simulates a self-contained environmental cooling core using a Peltier module and vortex-style dispersion fan.
    """

    def __init__(self, unit_id: str, power_input_watts: float, ambient_temp_c: float = 45.0):
        """
        Initialize the CryoCore unit.
        :param unit_id: Unique ID for this core
        :param power_input_watts: Available input power (e.g. solar, piston, battery)
        :param ambient_temp_c: Starting outside temperature in Celsius
        """
        self.unit_id = unit_id
        self.power_input_watts = power_input_watts
        self.ambient_temp_c = ambient_temp_c
        self.cooling_capacity_watts = 0.0
        self.operational = False
        self.internal_temp_c = ambient_temp_c  # Initial temp
        self.min_operating_power = 5.0  # Watts
        self.max_cooling_delta_c = 25.0  # Max drop

    def startup_sequence(self):
        if self.power_input_watts >= self.min_operating_power:
            self.operational = True
            self.calculate_cooling_capacity()
            print(f"[{self.unit_id}] CryoCore started.")
        else:
            print(f"[{self.unit_id}] Insufficient power to start (needs {self.min_operating_power}W).")

    def calculate_cooling_capacity(self):
        """
        Estimate cooling power (watts) based on input power and efficiency curve.
        """
        efficiency = 0.15  # Placeholder for real Peltier or hybrid thermal conversion
        self.cooling_capacity_watts = self.power_input_watts * efficiency

    def cool_environment(self, seconds: int = 60):
        """
        Simulate environmental cooling over time.
        Reduces internal temp to a max of (ambient - delta).
        """
        if not self.operational:
            print(f"[{self.unit_id}] Unit not running.")
            return

        delta_per_second = (self.cooling_capacity_watts / 1000.0) * 0.2  # Simulated scale
        target_temp = self.ambient_temp_c - self.max_cooling_delta_c

        for _ in range(seconds):
            if self.internal_temp_c > target_temp:
                self.internal_temp_c -= delta_per_second
            else:
                break
            time.sleep(0.01)  # Fast sim step

        print(f"[{self.unit_id}] Cooled to {self.internal_temp_c:.2f}°C")

    def shutdown_sequence(self):
        self.operational = False
        print(f"[{self.unit_id}] CryoCore shut down.")

    def status(self) -> dict:
        return {
            "unit_id": self.unit_id,
            "operational": self.operational,
            "input_power_watts": self.power_input_watts,
            "cooling_capacity_watts": self.cooling_capacity_watts,
            "internal_temp_c": self.internal_temp_c
        }
