# File: /opencryocore/core/cooling_model.py

import math

class CoolingModel:
    """
    Models the conversion of electrical power into ambient cooling.
    Used to simulate temperature drop in a given air volume per watt applied.
    """

    def __init__(self, air_volume_m3: float, system_efficiency: float = 0.68):
        """
        :param air_volume_m3: Volume of air being cooled (m³)
        :param system_efficiency: 0.0 - 1.0 cooling efficiency factor
        """
        self.air_volume_m3 = air_volume_m3
        self.system_efficiency = system_efficiency
        self.air_specific_heat_j_per_kg_c = 1005  # J/kg·°C (typical for dry air)
        self.air_density_kg_per_m3 = 1.2  # at sea level

    def compute_temp_drop(self, watts_input: float, seconds: int = 60) -> float:
        """
        Estimate temperature drop based on wattage input and efficiency.
        :param watts_input: Power applied (in watts)
        :param seconds: Duration of application
        :return: Estimated °C drop in air mass
        """
        total_joules = watts_input * seconds * self.system_efficiency
        air_mass = self.air_volume_m3 * self.air_density_kg_per_m3
        delta_temp_c = total_joules / (air_mass * self.air_specific_heat_j_per_kg_c)
        return delta_temp_c

    def inverse_temp_gain(self, watts_loss: float, seconds: int = 60, sunlight_factor: float = 1.0) -> float:
        """
        Estimate ambient re-heating from solar or ambient convection.
        :param watts_loss: Passive gain from external sources (e.g. solar)
        :param seconds: Time simulated
        :param sunlight_factor: 0.0 to 1.0 scale of sun exposure
        :return: Estimated °C increase
        """
        total_gain = watts_loss * seconds * sunlight_factor
        air_mass = self.air_volume_m3 * self.air_density_kg_per_m3
        delta_temp_c = total_gain / (air_mass * self.air_specific_heat_j_per_kg_c)
        return delta_temp_c
