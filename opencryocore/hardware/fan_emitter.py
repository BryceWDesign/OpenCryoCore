# File: /opencryocore/hardware/fan_emitter.py

class FanEmitter:
    """
    Models a fan-based air vortex emitter for CryoCore,
    designed to push cooled air radially in a 360-degree pattern.
    """

    def __init__(self, max_rpm: int = 3000, airflow_cfm: float = 150.0):
        """
        :param max_rpm: Maximum rotations per minute of the fan
        :param airflow_cfm: Airflow in cubic feet per minute
        """
        self.max_rpm = max_rpm
        self.airflow_cfm = airflow_cfm
        self.current_rpm = 0
        self.active = False

    def activate(self, duration_sec: int):
        """
        Activates the fan at max RPM for the specified duration.
        """
        self.current_rpm = self.max_rpm
        self.active = True
        print(f"[FanEmitter] Activated at {self.current_rpm} RPM for {duration_sec} seconds.")

    def shutdown(self):
        """
        Shuts down the fan.
        """
        self.current_rpm = 0
        self.active = False
        print("[FanEmitter] Shutdown.")

    def get_status(self) -> dict:
        """
        Returns current status of the fan emitter.
        """
        return {
            "active": self.active,
            "current_rpm": self.current_rpm,
            "max_rpm": self.max_rpm,
            "airflow_cfm": self.airflow_cfm
        }
