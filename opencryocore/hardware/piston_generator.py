# File: /opencryocore/hardware/piston_generator.py

import random
import time

class PistonGenerator:
    """
    Simulates a kinetic energy harvesting generator.
    Inspired by shake flashlights and drone-inspired pulse pistons.
    Converts motion, vibration, or rotational force into electrical output.
    """

    def __init__(self, efficiency: float = 0.35, max_output_watts: float = 15.0):
        """
        :param efficiency: Harvesting efficiency (0.0 - 1.0)
        :param max_output_watts: Theoretical max power output under ideal force
        """
        self.efficiency = efficiency
        self.max_output_watts = max_output_watts
        self.active = False
        self.current_output = 0.0

    def activate(self):
        self.active = True
        print("[PistonGenerator] Activated.")

    def shutdown(self):
        self.active = False
        self.current_output = 0.0
        print("[PistonGenerator] Shutdown.")

    def simulate_impact(self, force_level: float):
        """
        Simulates a kinetic event (shake, hit, pulse, or drone thrash).
        :param force_level: 0.0 - 1.0 scale of impulse strength
        """
        if not self.active:
            return 0.0
        power_generated = self.max_output_watts * self.efficiency * force_level
        self.current_output = power_generated
        return power_generated

    def get_current_output(self):
        """
        :return: Current generated power in watts
        """
        return self.current_output

    def test_random_input(self, duration_sec: int = 5):
        """
        Run a quick test simulating random drone vibration or shaking.
        """
        self.activate()
        for _ in range(duration_sec):
            force = random.uniform(0.2, 1.0)
            power = self.simulate_impact(force)
            print(f"[PistonGenerator] Force: {force:.2f} → {power:.2f} W")
            time.sleep(1)
        self.shutdown()
