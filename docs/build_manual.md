# OpenCryoCore Build Manual  
Version 1.0 | Project Borealis  
Licensed under Apache 2.0

---

## Contents

1. Overview  
2. Required Tools  
3. Hardware Bill of Materials  
4. Enclosure Assembly  
5. Thermoelectric Cooler Mounting  
6. Fan + Air Emitter Setup  
7. Power & Battery Wiring  
8. Microcontroller + Software Setup  
9. Final Assembly  
10. Installation + Deployment  
11. Maintenance & Notes

---

## 1. Overview

This guide explains how to build a single operational OpenCryoCore node, capable of cooling a 9-foot outdoor zone by approximately 3°F continuously.

The unit is designed to mount on a pole (or tripod) and operate independently using solar + battery + kinetic power sources. The container is built around a vacuum-insulated metallic housing with radial airflow from a 360° fan emitter.

---

## 2. Required Tools

- Screwdriver set (Phillips, Torx)
- Soldering iron + solder
- Wire strippers + crimp tool
- Heat gun (for heat shrink)
- M3 and M4 hex key set
- Dremel or rotary cutter (for vent holes)
- Digital multimeter
- Drill with metal bits
- Thermal paste

---

## 3. Hardware Bill of Materials

| Component                       | Qty | Description/Source Suggestion                     |
|--------------------------------|-----|--------------------------------------------------|
| Raspberry Pi Zero 2 W          | 1   | or any 5V SBC with GPIO support                  |
| TEC1-12706 Peltier Cooler      | 2   | 12V, 60W thermoelectric coolers                  |
| Heatsink + fan combo           | 2   | Must match size of TECs                          |
| Stainless steel thermal flask  | 1   | 40–64oz vacuum-insulated (e.g., Contigo)         |
| Radial fan (12V, 3000 RPM)     | 1   | 360° shroud fan                                  |
| 12V LiFePO₄ battery (200Wh)    | 1   | with BMS protection                              |
| 100W flexible solar panel      | 1   | rollable or rigid                                |
| Piston generator (DIY or kit)  | 1   | adapted shake flashlight coil-magnet piston      |
| DC-DC Step-Down Converter      | 1   | 12V input to 5V output                           |
| Voltage & Temp Sensors         | 2   | DS18B20, INA219 recommended                      |
| Mounting bracket               | 1   | for light pole or tripod                         |
| Wires, connectors, fasteners   | —   | 18AWG+ wire, JST, XT60, M3 screws                |
| Weather-sealant grommets       | 4   | for cable exits                                  |

---

## 4. Enclosure Assembly

- Cut bottom vent holes in the thermal flask for airflow using rotary tool
- Drill 4x screw mounts inside for fan emitter ring
- Add grommets for power/sensor wiring near base
- Optionally coat interior with thermal dispersion ceramic layer

---

## 5. Thermoelectric Cooler Mounting

- Sandwich TEC between heatsink+fan on one side (hot), and cold plate facing interior
- Use thermal paste liberally on both sides
- Screw into custom aluminum cold plate or direct-to-lid mount
- Route wires neatly to power chamber

—

## 6. Fan + Air Emitter Setup

- Mount radial fan inside lid or base, aligned to blow across cold surface
- Ensure 360° airflow via diffuser ring
- Secure with vibration-dampening standoffs
- Test airflow coverage using smoke or IR thermometer

—

## 7. Power & Battery Wiring

- Connect solar panel to charge controller → battery
- Connect piston generator to battery BMS (low-voltage recharge line)
- Add DC-DC buck converter to step down 12V → 5V for Pi and sensors
- Add 12V fan and TEC on switched relay GPIO
- Fuse all high-current lines appropriately

—

## 8. Microcontroller + Software Setup

- Flash Raspberry Pi with Raspberry Pi OS Lite
- Enable I2C, SPI, and GPIO via raspi-config
- Clone the OpenCryoCore repo:
  ```bash
  git clone https://github.com/<your-org>/OpenCryoCore
  
Install Python dependencies: pip install flask

Run the main control loop and dashboard: python3 display/web_dashboard.py

—

9. Final Assembly
Route wires cleanly and use heat shrink

Weatherproof all grommet exits

Mount flask on pole using bracket

Position solar panel with max sun exposure

Power on and monitor via dashboard

—

10. Installation + Deployment
Install units minimum 12 ft apart for optimal radius coverage

Avoid installing in shaded zones unless ambient airflow is high

Ideal configuration: 1 pole per 450 ft² public square

Combine 9 poles into one HyperPole (cluster formation)

—

11. Maintenance & Notes
Clean dust/debris from fan and vent monthly

Recalibrate sensors quarterly

Piston generator components may require annual rebuilds

Dashboard reachable over local network (port 8080)

Battery replacement expected after 3–5 years

—

Project is 100% open-source and field-buildable using common tools and online parts. For questions, post Issues on the GitHub repo.
