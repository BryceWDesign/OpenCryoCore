# File: /opencryocore/hardware/power_interface.py

class PowerSourceType:
    SOLAR = "solar"
    PISTON = "piston"
    GRID = "grid"
    BATTERY = "battery"


class PowerInterface:
    """
    Hardware-agnostic power interface for delivering energy to CryoCore systems.
    Handles different sources (solar panel, piston generator, AC grid, battery) and simulates output.
    """

    def __init__(self, source_type: str, max_output_watts: float):
        """
        :param source_type: Source of power ("solar", "piston", "grid", "battery")
        :param max_output_watts: Maximum wattage this source can deliver
        """
        self.source_type = source_type
        self.max_output_watts = max_output_watts
        self.active = False

    def activate(self):
        self.active = True
        print(f"[PowerInterface] {self.source_type} source activated.")

    def shutdown(self):
        self.active = False
        print(f"[PowerInterface] {self.source_type} source shut down.")

    def get_current_output(self, time_of_day: float = 12.0, piston_rate: float = 1.0) -> float:
        """
        Returns current output power in watts depending on source behavior:
        - Solar: varies by time of day (simulate noon = max, morning/evening = less)
        - Piston: varies by piston rate (e.g. user motion or kinetic charge)
        - Grid: always max
        - Battery: always max until depleted (depletion not simulated here)

        :param time_of_day: Simulated time (0.0 - 24.0)
        :param piston_rate: 0.0 - 1.0 efficiency scale
        :return: current power output in watts
        """
        if not self.active:
            return 0.0

        if self.source_type == PowerSourceType.SOLAR:
            sun_factor = max(0.0, 1.0 - abs(time_of_day - 12.0) / 6.0)
            return self.max_output_watts * sun_factor

        elif self.source_type == PowerSourceType.PISTON:
            return self.max_output_watts * piston_rate

        elif self.source_type == PowerSourceType.GRID:
            return self.max_output_watts

        elif self.source_type == PowerSourceType.BATTERY:
            return self.max_output_watts

        return 0.0
