# File: /opencryocore/hardware/structure_shell.py

class StructureShell:
    """
    Represents the metallic shell enclosure modeled on Contigo insulated container design,
    modified for inverted operation to enhance heat absorption and cold air retention.
    """

    def __init__(self, material: str = "stainless_steel", thickness_mm: float = 2.0, volume_liters: float = 3.0):
        """
        :param material: Shell material (default stainless steel for durability and thermal properties)
        :param thickness_mm: Thickness of the metal shell in millimeters
        :param volume_liters: Internal volume capacity of the shell (affects cooling potential)
        """
        self.material = material
        self.thickness_mm = thickness_mm
        self.volume_liters = volume_liters

        # Thermal conductivity coefficients (W/m·K) approximate values
        self.material_conductivity = {
            "stainless_steel": 16,
            "aluminum": 205,
            "copper": 385
        }
        self.conductivity = self.material_conductivity.get(self.material, 16)

    def heat_transfer_rate(self, delta_temp_c: float) -> float:
        """
        Calculates the heat transfer rate (Watts) through the shell for given temperature difference.
        Simplified steady-state conduction model.

        :param delta_temp_c: Temperature difference across shell (°C)
        :return: Heat transfer rate in Watts
        """
        # Simplified conduction assuming flat plate: Q = k * A * ΔT / d
        # Approximating surface area from volume (cylindrical approx)
        radius_m = ( (3 * self.volume_liters / 1000) / (3.1416 * 1) ) ** (1/2)
        surface_area_m2 = 2 * 3.1416 * radius_m * 1 + 2 * 3.1416 * (radius_m ** 2)  # lateral + ends
        thickness_m = self.thickness_mm / 1000

        heat_rate_watts = (self.conductivity * surface_area_m2 * delta_temp_c) / thickness_m
        return heat_rate_watts

    def __str__(self):
        return (f"StructureShell(material={self.material}, thickness_mm={self.thickness_mm}, "
                f"volume_liters={self.volume_liters}, conductivity={self.conductivity} W/m·K)")
