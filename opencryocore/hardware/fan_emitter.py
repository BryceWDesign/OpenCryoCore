# File: /opencryocore/hardware/fan_emitter.py

import time

class FanEmitter:
    """
    Controls high-efficiency pulse fan modules used to radiate cooled air in all directions.
    Simulates vortex output for 360° radial dispersion and upward projection.
    """

    def __init__(self, num_emitters: int = 8, max_power_watts: float = 40.0):
        """
        :param num_emitters: Number of fan units installed around the ring
        :param max_power_watts: Maximum power dedicated to fan thrust
        """
        self.num_emitters = num_emitters
        self.max_power_watts = max_power_watts
        self.operating = False

    def activate(self, duration_sec: int = 10):
        """
        Simulate active fan output.
        """
        if self.operating:
            print("[FanEmitter] Already running.")
            return

        self.operating = True
        power_per_fan = self.max_power_watts / self.num_emitters
        print(f"[FanEmitter] Emitting vortex cooling using {self.num_emitters} fans.")
        for i in range(duration_sec):
            print(f"  • Emission cycle {i+1}/{duration_sec} | Output: {power_per_fan:.2f} W/fan")
            time.sleep(1)
        self.operating = False
        print("[FanEmitter] Emission complete.")

    def shutdown(self):
        self.operating = False
        print("[FanEmitter] All fans shut down.")

    def get_status(self) -> dict:
        return {
            "emitters": self.num_emitters,
            "max_power_watts": self.max_power_watts,
            "operating": self.operating
        }
