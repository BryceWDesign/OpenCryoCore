# File: /opencryocore/display/web_dashboard.py

from flask import Flask, jsonify, render_template
from opencryocore.control.core_controller import CryoCoreController
import threading

app = Flask(__name__)
controller = CryoCoreController(cluster_id="default_cluster")

# Run controller in separate thread to keep web server responsive
def start_controller():
    controller.initialize()
    controller.run_loop(cycle_seconds=10)

controller_thread = threading.Thread(target=start_controller, daemon=True)
controller_thread.start()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/status')
def status():
    status_data = controller.get_status()
    return jsonify(status_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
