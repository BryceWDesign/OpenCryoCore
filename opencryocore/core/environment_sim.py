# File: /opencryocore/core/environment_sim.py

import random
import math

class EnvironmentSim:
    """
    Simulates the ambient outdoor environment affected by CryoCore units.
    Tracks temperature changes, diffusion, and radius of impact over time.
    """

    def __init__(self, initial_temp_c: float = 45.0, radius_ft: float = 9.0, height_ft: float = 20.0):
        """
        :param initial_temp_c: Starting ambient temperature
        :param radius_ft: Radius of cooling influence (ft)
        :param height_ft: Height of air column affected (ft)
        """
        self.initial_temp_c = initial_temp_c
        self.current_temp_c = initial_temp_c
        self.radius_ft = radius_ft
        self.height_ft = height_ft
        self.air_volume_m3 = self._calculate_air_volume()

    def _calculate_air_volume(self) -> float:
        """
        Calculate the cylindrical air volume affected by the CryoCore unit.
        :return: volume in cubic meters
        """
        radius_m = self.radius_ft * 0.3048
        height_m = self.height_ft * 0.3048
        return math.pi * (radius_m ** 2) * height_m

    def apply_cooling(self, cooling_watts: float, seconds: int = 60):
        """
        Simulate temperature reduction from CryoCore over time.
        :param cooling_watts: Total watts applied to this environment
        :param seconds: Cooling duration
        """
        specific_heat_air_j_per_kg_c = 1005  # J/kg·°C
        air_density_kg_per_m3 = 1.2  # at sea level
        total_air_mass = self.air_volume_m3 * air_density_kg_per_m3

        energy_removed_joules = cooling_watts * seconds
        temp_drop_c = energy_removed_joules / (total_air_mass * specific_heat_air_j_per_kg_c)

        self.current_temp_c = max(0.0, self.current_temp_c - temp_drop_c)

    def recover_heat(self, seconds: int = 60, sunlight_factor: float = 1.0):
        """
        Simulates heat gain when CryoCore is off, driven by solar and convection.
        :param seconds: Time to simulate
        :param sunlight_factor: 0.0 (night) to 1.0 (midday)
        """
        passive_gain_per_sec = 0.005 * sunlight_factor  # °C/sec
        self.current_temp_c += passive_gain_per_sec * seconds
        self.current_temp_c = min(self.current_temp_c, self.initial_temp_c)

    def report(self) -> dict:
        return {
            "ambient_temp_start_c": self.initial_temp_c,
            "current_temp_c": self.current_temp_c,
            "radius_ft": self.radius_ft,
            "height_ft": self.height_ft,
            "air_volume_m3": round(self.air_volume_m3, 2)
        }
