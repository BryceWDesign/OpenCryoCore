# OpenCryoCore: Project Borealis — Outdoor Cryogenic Cooling System

## Overview

OpenCryoCore is an open-source initiative to build a high-performance outdoor cooling device designed to reduce ambient air temperature by up to 3°F (1.7°C) within a 9-foot radius continuously. Inspired by thermoelectric cooling (Peltier effect), ambient kinetic energy harvesting, and innovative air dispersion methods, this system targets localized cooling to combat extreme heat conditions such as those experienced in Lake Havasu City, Arizona.

The system integrates:
- Thermoelectric modules for solid-state cooling
- Metallic shell design inspired by vacuum-insulated containers for thermal retention
- High-speed piston-based kinetic energy harvesters (shake flashlight tech adapted)
- 360-degree fan-driven air vortex emitters
- Scalable cluster management to expand cooled zones
- Real-time monitoring dashboard for system status and environmental simulation

## Features

- Continuous cooling with minimal moving parts
- Renewable energy integration (solar + kinetic)
- Modular hardware and software architecture
- Designed for outdoor installation (e.g., lamp post-sized units)
- Open-source with commercial-friendly Apache 2.0 License

## Goals

- Reduce temperature by 3°F within a 9-foot radius, sustained while powered
- Scalable deployment: clusters of 9 units form hyperpoles; clusters of hyperpoles expand coverage
- Provide a platform for further research into urban heat mitigation

## Build Instructions

### Hardware Components

- Raspberry Pi (or equivalent microcontroller)
- Thermoelectric cooler modules (Peltier devices)
- Metallic vacuum-insulated shell (based on modified Contigo thermal flask)
- High-speed fan capable of 3000 RPM with 360-degree airflow
- Piston generator assembly adapted from kinetic energy harvesting designs
- Solar panels and battery pack for power management

### Software Setup

1. Clone the repository to your local machine.
2. Install Python 3.8+.
3. Install required Python packages:
   ```bash
   pip install flask
Navigate to the /opencryocore directory.

Run the web dashboard to monitor system status: python display/web_dashboard.py

The dashboard is accessible at http://<device_ip>:8080.

Operational Notes
The CryoCoreController runs the main control loop managing cooling and power.

HyperPoleClusters enable modular scaling by coordinating multiple units.

EnvironmentSim models the temperature changes within the target air volume.

License
This project is licensed under the Apache License 2.0 — free to use, modify, and sell with attribution. You are protected under this license while contributing or distributing derived works.

Contribution Guidelines
Please fork the repository and submit pull requests for improvements.

Report bugs or request features via GitHub Issues.

Maintain coding standards and include tests for new functionality.

Acknowledgements
Inspired by Nikola Tesla’s visionary principles and modern advancements in thermoelectric cooling and ambient energy harvesting.

OpenCryoCore — Cooling the future, one degree at a time.
