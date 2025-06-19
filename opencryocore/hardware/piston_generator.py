# File: /opencryocore/hardware/piston_generator.py

import random
import time

class PistonGenerator:
    """
    Simulates a piston-based kinetic energy harvester.
    Converts mechanical movement into electrical power for CryoCore.
    """

    def __init__(self, max_output_watts: float = 50.0):
        """
        :param max_output_watts: Maximum power output achievable (W)
        """
        self.max_output_watts = max_output_watts
        self.current_output = 0.0
        self.active = False

    def activate(self):
        """
        Starts the piston generator simulation.
        """
        self.active = True
        print("[PistonGenerator] Activated.")

    def simulate_impact(self, force_level: float = 1.0):
        """
        Simulates an impact event generating power.
        :param force_level: Relative force from 0.0 to 1.0 representing intensity of piston impact
        """
        if not self.active:
            print("[PistonGenerator] Not active. Impact ignored.")
            return

        # Generate power output proportionally to force, with some randomness
        output = force_level * self.max_output_watts * (0.8 + 0.4 * random.random())
        self.current_output = min(output, self.max_output_watts)
        print(f"[PistonGenerator] Impact simulated: output {self.current_output:.2f} W.")

    def get_current_output(self) -> float:
        """
        Returns the current power output in watts.
        """
        return self.current_output

    def shutdown(self):
        """
        Stops the piston generator.
        """
        self.active = False
        self.current_output = 0.0
        print("[PistonGenerator] Shutdown.")
