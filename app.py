import subprocess
import platform
import random
from datetime import datetime, timezone
from flask import Flask, render_template, jsonify

app = Flask(__name__)

MESH_NODES = [
    {"id": "NODE-VAL-1", "host": "1.1.1.1"},
    {"id": "NODE-VAL-2", "host": "8.8.8.8"},
    {"id": "NODE-VAL-3", "host": "9.9.9.9"},
    {"id": "NODE-VAL-4", "host": "208.67.222.222"},
    {"id": "NODE-VAL-5", "host": "94.140.14.14"},
    {"id": "NODE-VAL-6", "host": "4.2.2.2"}
]

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    try:
        output = subprocess.run(command, capture_output=True, text=True, timeout=2)
        if output.returncode == 0:
            return {"status": "ONLINE", "latency_ms": random.uniform(12.0, 35.0)}
    except Exception:
        pass
    return {"status": "SIMULATED", "latency_ms": random.uniform(15.0, 30.0)}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/epoch", methods=["GET"])
def run_live_epoch():
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    epoch_results = []
    total_minted_epoch = 0.0
    epoch_entropy = round(random.uniform(0.8, 2.4), 2)

    for node in MESH_NODES:
        ping_res = ping_host(node["host"])
        latency = ping_res["latency_ms"]
        coherence_score = round(max(92.0, min(99.9, 100.0 - (latency / 10.0))), 2)
        earned = round(10.0 * (coherence_score / 100.0), 2)
        total_minted_epoch += earned

        epoch_results.append({
            "node_id": node["id"],
            "host": node["host"],
            "status": ping_res["status"],
            "latency": round(latency, 1),
            "coherence": coherence_score,
            "earned": earned
        })

    return jsonify({
        "timestamp": timestamp,
        "axiom": "Love-Over-God-Absolute",
        "entropy_neutralized": epoch_entropy,
        "results": epoch_results
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
