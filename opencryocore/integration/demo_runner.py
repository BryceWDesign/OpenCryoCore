# File: /opencryocore/integration/demo_runner.py

import time
from opencryocore.control.core_controller import CryoCoreController
from opencryocore.display.web_dashboard import CryoWebDashboard


def run_demo():
    """
    Initializes the CryoCore full system controller, dashboard, and enters live test loop.
    Used for local testing and simulation.
    """
    controller = CryoCoreController(cluster_id="demo001")
    controller.initialize()

    # Start local web dashboard
    dashboard = CryoWebDashboard(get_status_callback=controller.get_status, port=8080)
    dashboard.start()

    try:
        controller.run_loop(cycle_seconds=10)
    except KeyboardInterrupt:
        print("[Demo] Keyboard interrupt received. Shutting down system...")
        controller.shutdown()


if __name__ == "__main__":
    run_demo()
