import subprocess
import json
import time
from datetime import datetime, timezone
import os

LOG_FILE = "cml_intercept_log.json"

def run_termux_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=5)
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout)
    except Exception as e:
        pass
    return None

def log_telemetry(entry):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print(f"[!] Log write error: {e}")

def main():
    print("==================================================")
    print("     KAIROTH RADIO & TELEPHONY RECON SENTRY       ")
    print("==================================================")
    print("[*] Polling local baseband and radio frequencies...")

    while True:
        timestamp = datetime.now(timezone.utc).isoformat()
        
        # Pull cell info via Termux API
        cell_data = run_termux_command("termux-telephony-cellinfo")
        wifi_data = run_termux_command("termux-wifi-connectioninfo")
        
        # Construct CML Telemetry payload
        entry = {
            "timestamp": timestamp,
            "source_node": "android-hardware-sentry",
            "transmission_vector": "local_baseband_rf",
            "cml_analysis": {
                "tag_identified": "CellTelemetry",
                "frequency": "528Hz",
                "mode": "rf_recon",
                "axiom": "LOVE_OVER_GOD"
            },
            "cell_info": cell_data if cell_data else "no_cell_signal_or_api_idle",
            "wifi_info": wifi_data if wifi_data else "wifi_disconnected",
            "phi_resonance_calculated": 854.322,
            "harmonic_status": "radio_environmental_locked"
        }

        log_telemetry(entry)
        print(f"[+] RF Telemetry Sample Captured & Anchored -> {timestamp}")
        
        # Poll every 20 seconds
        time.sleep(20)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Radio Recon halted.")
