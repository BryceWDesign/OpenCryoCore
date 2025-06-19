# File: /opencryocore/core/cooling_model.py

class CoolingModel:
    """
    Models the thermoelectric cooling effect using Peltier devices.
    Calculates temperature drop in the target air volume based on input power and duration.
    """

    def __init__(self, air_volume_m3: float):
        """
        :param air_volume_m3: Volume of air to be cooled in cubic meters
        """
        self.air_volume_m3 = air_volume_m3
        self.air_density_kg_per_m3 = 1.225  # average air density at sea level (kg/m³)
        self.specific_heat_capacity_air = 1005  # J/(kg·K)

    def compute_temp_drop(self, power_watts: float, seconds: int) -> float:
        """
        Calculates approximate temperature drop (°C) given power and duration.
        Assumes all power goes into cooling.

        Q = m * c * ΔT  => ΔT = Q / (m * c)
        where Q = power_watts * seconds (Joules)
        m = air_density * volume

        :param power_watts: Cooling power input in watts
        :param seconds: Duration cooling applied in seconds
        :return: Temperature drop in °C
        """
        energy_joules = power_watts * seconds
        mass_air = self.air_density_kg_per_m3 * self.air_volume_m3
        temp_drop = energy_joules / (mass_air * self.specific_heat_capacity_air)
        return temp_drop

    def inverse_temp_gain(self, heat_watts: float, seconds: int) -> float:
        """
        Models temperature increase from ambient heat gain.
        :param heat_watts: Heat gained in watts
        :param seconds: Duration in seconds
        :return: Temperature increase in °C
        """
        energy_joules = heat_watts * seconds
        mass_air = self.air_density_kg_per_m3 * self.air_volume_m3
        temp_gain = energy_joules / (mass_air * self.specific_heat_capacity_air)
        return temp_gain
