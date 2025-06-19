# File: /opencryocore/display/oled_driver.py

import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class OLEDStatusDisplay:
    """
    Displays real-time CryoCore status on a 128x64 I2C OLED screen.
    Compatible with SSD1306 displays via Adafruit driver and CircuitPython.
    """

    def __init__(self, get_status_callback, i2c_address=0x3C):
        """
        :param get_status_callback: Function that returns a dict of system values
        :param i2c_address: I2C address of the OLED screen (default 0x3C)
        """
        self.get_status = get_status_callback
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(128, 64, self.i2c, addr=i2c_address)
        self.display.fill(0)
        self.display.show()

        self.image = Image.new("1", (128, 64))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()

    def update_display(self):
        """
        Pull latest status and render to the OLED.
        """
        status = self.get_status()
        self.draw.rectangle((0, 0, 128, 64), outline=0, fill=0)

        lines = [
            f"Cluster: {status.get('cluster_id', '---')}",
            f"Op: {'ON' if status.get('operational') else 'OFF'}",
            f"Temp: {status.get('ambient_temp_c', '--')} C",
        ]

        for i, line in enumerate(lines):
            self.draw.text((0, i * 10), line, font=self.font, fill=255)

        self.display.image(self.image)
        self.display.show()

    def run_loop(self, refresh_interval_sec=2):
        """
        Keep updating the display every few seconds.
        """
        while True:
            self.update_display()
            time.sleep(refresh_interval_sec)
