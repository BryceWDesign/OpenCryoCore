# File: /opencryocore/core/thermal_memory.py

import time

class ThermalMemory:
    """
    Simulates the thermal retention behavior of cooled air volumes.
    Enables CryoCore to "coast" between active cooling cycles without immediate temperature rebound.
    """

    def __init__(self, memory_half_life_sec: int = 300):
        """
        :param memory_half_life_sec: Time it takes for the cooled air to lose 50% of its thermal benefit (in seconds)
        """
        self.last_cool_timestamp = time.time()
        self.last_temp_c = None
        self.memory_half_life_sec = memory_half_life_sec

    def record_temp(self, temp_c: float):
        """
        Stores the last temperature after active cooling.
        """
        self.last_temp_c = temp_c
        self.last_cool_timestamp = time.time()
        print(f"[ThermalMemory] Temperature memory updated: {temp_c:.2f}°C")

    def get_estimated_temp(self, ambient_temp_c: float) -> float:
        """
        Returns an estimated current temp based on thermal decay over time.
        :param ambient_temp_c: Outside uncontrolled ambient temperature
        :return: Estimated temperature in the cold zone
        """
        if self.last_temp_c is None:
            return ambient_temp_c

        elapsed = time.time() - self.last_cool_timestamp
        decay_factor = 0.5 ** (elapsed / self.memory_half_life_sec)
        estimated_temp = self.last_temp_c + (ambient_temp_c - self.last_temp_c) * (1 - decay_factor)

        return round(estimated_temp, 2)
