# File: /opencryocore/hardware/power_interface.py

class PowerInterface:
    """
    Manages power input sources and distribution for CryoCore hardware.
    Supports batteries, solar panels, and load regulation.
    """

    def __init__(self, battery_capacity_wh: float = 200.0, solar_panel_watts: float = 100.0):
        """
        :param battery_capacity_wh: Total battery capacity in watt-hours
        :param solar_panel_watts: Peak solar panel output in watts
        """
        self.battery_capacity_wh = battery_capacity_wh
        self.solar_panel_watts = solar_panel_watts
        self.battery_level_wh = battery_capacity_wh
        self.load_watts = 0.0
        self.operational = False

    def power_on(self):
        self.operational = True
        print("[PowerInterface] Power system online.")

    def power_off(self):
        self.operational = False
        self.load_watts = 0.0
        print("[PowerInterface] Power system offline.")

    def consume_power(self, watts: float, duration_hours: float):
        """
        Consume power from battery based on load and duration.
        :param watts: Power load in watts
        :param duration_hours: Duration in hours
        """
        if not self.operational:
            return
        energy_consumed = watts * duration_hours
        self.battery_level_wh = max(self.battery_level_wh - energy_consumed, 0.0)
        print(f"[PowerInterface] Consumed {energy_consumed:.2f} Wh. Battery level: {self.battery_level_wh:.2f} Wh.")

    def charge_battery(self, duration_hours: float):
        """
        Charge battery using solar panel output.
        :param duration_hours: Duration in hours
        """
        if not self.operational:
            return
        energy_generated = self.solar_panel_watts * duration_hours
        self.battery_level_wh = min(self.battery_level_wh + energy_generated, self.battery_capacity_wh)
        print(f"[PowerInterface] Charged {energy_generated:.2f} Wh. Battery level: {self.battery_level_wh:.2f} Wh.")

    def get_battery_status(self) -> dict:
        return {
            "battery_capacity_wh": self.battery_capacity_wh,
            "battery_level_wh": self.battery_level_wh,
            "solar_panel_watts": self.solar_panel_watts,
            "operational": self.operational
        }
