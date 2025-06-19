# File: /opencryocore/core/environment_sim.py

import time
from opencryocore.core.cooling_model import CoolingModel
from opencryocore.core.thermal_memory import ThermalMemory

class EnvironmentSim:
    """
    Simulates the outdoor environment temperature within the CryoCore's target radius.
    Accounts for cooling input, thermal memory, and ambient heat gain (e.g. solar).
    """

    def __init__(self, initial_temp_c: float = 40.0, radius_ft: float = 9.0, height_ft: float = 20.0):
        """
        :param initial_temp_c: Starting ambient temperature in °C
        :param radius_ft: Radius of cooled air volume in feet
        :param height_ft: Vertical height of cooled air volume in feet
        """
        self.initial_temp_c = initial_temp_c
        self.radius_ft = radius_ft
        self.height_ft = height_ft

        self.air_volume_m3 = self._calculate_air_volume_m3(radius_ft, height_ft)
        self.cooling_model = CoolingModel(self.air_volume_m3)
        self.thermal_memory = ThermalMemory(memory_half_life_sec=300)

        self.current_temp_c = initial_temp_c
        self.last_update_time = time.time()

    def _calculate_air_volume_m3(self, radius_ft: float, height_ft: float) -> float:
        """
        Calculates the volume of air being cooled (cylindrical volume in cubic meters).
        """
        radius_m = radius_ft * 0.3048
        height_m = height_ft * 0.3048
        volume = 3.1416 * (radius_m ** 2) * height_m
        return volume

    def apply_cooling(self, cooling_watts: float, seconds: int):
        """
        Applies cooling effect based on power input and elapsed time.
        """
        temp_drop = self.cooling_model.compute_temp_drop(cooling_watts, seconds)
        self.current_temp_c = max(self.current_temp_c - temp_drop, -273.15)  # prevent below absolute zero
        self.thermal_memory.record_temp(self.current_temp_c)
        self.last_update_time = time.time()

    def recover_heat(self, seconds: int, ambient_temp_c: float = None):
        """
        Models ambient heat gain and temperature rebound over time.
        """
        ambient_temp_c = ambient_temp_c if ambient_temp_c is not None else self.initial_temp_c
        heat_gain_watts = 300  # Estimated solar + ambient gain in watts; tune as needed
        temp_gain = self.cooling_model.inverse_temp_gain(heat_gain_watts, seconds)
        self.current_temp_c = min(self.current_temp_c + temp_gain, ambient_temp_c)
        self.last_update_time = time.time()

    def report(self) -> dict:
        """
        Returns current environment simulation status.
        """
        return {
            "current_temp_c": round(self.current_temp_c, 2),
            "radius_ft": self.radius_ft,
            "height_ft": self.height_ft,
            "air_volume_m3": round(self.air_volume_m3, 2),
            "last_update": self.last_update_time
        }
