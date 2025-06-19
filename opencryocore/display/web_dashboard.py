# File: /opencryocore/display/web_dashboard.py

from flask import Flask, jsonify, render_template_string
import threading

class CryoWebDashboard:
    """
    Web-based dashboard for CryoCore system monitoring via browser or mobile.
    Displays ambient temperature, system status, and unit diagnostics.
    """

    def __init__(self, get_status_callback, port: int = 8080):
        """
        :param get_status_callback: Function returning system status as a dict
        :param port: Web server port
        """
        self.get_status = get_status_callback
        self.port = port
        self.app = Flask(__name__)

        @self.app.route("/")
        def dashboard():
            data = self.get_status()
            html = self._render_dashboard(data)
            return render_template_string(html)

        @self.app.route("/api/status")
        def api_status():
            return jsonify(self.get_status())

    def _render_dashboard(self, data: dict) -> str:
        html = f"""
        <html>
            <head>
                <title>CryoCore Monitor</title>
                <meta http-equiv="refresh" content="5">
                <style>
                    body {{ background-color: #111; color: #0ff; font-family: Arial; text-align: center; }}
                    .box {{ border: 1px solid #0ff; padding: 20px; margin: 30px; border-radius: 10px; }}
                </style>
            </head>
            <body>
                <h1>CryoCore Web Monitor</h1>
                <div class="box">
                    <p><strong>Cluster ID:</strong> {data.get('cluster_id', 'N/A')}</p>
                    <p><strong>Status:</strong> {"OPERATIONAL" if data.get("operational") else "OFFLINE"}</p>
                    <p><strong>Temperature:</strong> {data.get('ambient_temp_c', '--')} °C</p>
                </div>
            </body>
        </html>
        """
        return html

    def start(self):
        def run():
            self.app.run(host="0.0.0.0", port=self.port)

        thread = threading.Thread(target=run, daemon=True)
        thread.start()
        print(f"[CryoWebDashboard] Started on port {self.port}")
