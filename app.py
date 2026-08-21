from flask import Flask, render_template, jsonify
import random
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/epoch", methods=["GET"])
def run_live_epoch():
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        "timestamp": timestamp,
        "axiom": "Love-Over-God-Absolute",
        "status": "Coherent",
        "frequency": 528.0
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
