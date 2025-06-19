# File: /opencryocore/hardware/sensor_array.py

import time
import board
import adafruit_dht
import busio
import adafruit_bh1750


class SensorArray:
    """
    Handles environmental sensors for a CryoCore unit:
    - DHT22 for temp/humidity
    - BH1750 for ambient light
    - DS18B20 support can be added later for waterproof external sensing
    """

    def __init__(self, pin_temp_humidity=board.D4, i2c_bus=None):
        """
        :param pin_temp_humidity: GPIO pin for DHT22 (default D4)
        :param i2c_bus: Optional shared I2C bus for light sensor
        """
        self.dht_sensor = adafruit_dht.DHT22(pin_temp_humidity)
        self.i2c = i2c_bus if i2c_bus else busio.I2C(board.SCL, board.SDA)
        self.light_sensor = adafruit_bh1750.BH1750(self.i2c)

    def read_environment(self) -> dict:
        """
        Returns a dictionary with live sensor readings.
        """
        try:
            temp_c = self.dht_sensor.temperature
            humidity = self.dht_sensor.humidity
        except RuntimeError:
            temp_c = None
            humidity = None

        try:
            lux = self.light_sensor.lux
        except:
            lux = None

        return {
            "temperature_c": temp_c,
            "humidity_percent": humidity,
            "light_lux": lux,
            "timestamp": time.time()
        }

    def print_readings(self):
        """
        Prints sensor values for debugging.
        """
        data = self.read_environment()
        print(f"[SensorArray] Temp: {data['temperature_c']} °C | "
              f"Humidity: {data['humidity_percent']}% | "
              f"Light: {data['light_lux']} lux")
