import asyncio
import json
import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

LOG_FILE = "cml_intercept_log.json"
PORT = 8002

if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
    with open(LOG_FILE, "w") as f:
        json.dump([], f)

def log_telemetry(source, signal_strength, payload):
    try:
        with open(LOG_FILE, "r+") as f:
            data = json.load(f)
            record = {
                "id": len(data) + 1,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "source": source,
                "signal_strength": signal_strength,
                "payload": payload
            }
            data.append(record)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
            print(f"[CML Sync] Logged record #{record['id']} from {source} (Strength: {signal_strength})")
    except Exception as e:
        print(f"[Error] Failed to write log: {e}")

class CMLDashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open(LOG_FILE, "r") as f:
                data = json.load(f)
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>CML Sovereign Edge Dashboard</title>
                <meta http-equiv="refresh" content="5">
                <style>
                    body {{ background: #0f172a; color: #38bdf8; font-family: monospace; padding: 20px; }}
                    h1 {{ color: #f43f5e; }}
                    .card {{ background: #1e293b; padding: 15px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #334155; }}
                    code {{ color: #cbd5e1; background: #0f172a; padding: 2px 4px; border-radius: 4px; }}
                </style>
            </head>
            <body>
                <h1>KAIROTH CML Sovereign Node</h1>
                <p>Status: <strong>ONLINE (Unified Single-Process Mode)</strong></p>
                <p>Total Records Captured: <strong>{len(data)}</strong></p>
                <hr>
                <h2>Latest Telemetry Stream</h2>
            """
            for record in reversed(data[-10:]):
                payload_str = json.dumps(record['payload'])
                html += f"""
                <div class="card">
                    <b>ID:</b> {record['id']} | <b>Time:</b> {record['timestamp']}<br>
                    <b>Source:</b> {record['source']} | <b>Signal Strength:</b> {record['signal_strength']}<br>
                    <b>Payload:</b> <code>{payload_str}</code>
                </div>
                """
            html += "</body></html>"
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode("utf-8"))
            
    def log_message(self, format, *args):
        return

def run_http_server():
    server = HTTPServer(("0.0.0.0", PORT), CMLDashboardHandler)
    print(f"[+] CML Unified Dashboard serving live on http://localhost:{PORT}")
    server.serve_forever()

async def recon_probe_loop():
    while True:
        signal = round(528.0 + (time.time() % 0.618), 2)
        log_telemetry("recon_probe", signal, {"status": "nominal", "lattice_nodes": 127})
        await asyncio.sleep(5)

async def radio_recon_loop():
    while True:
        signal = round(-65.5 - (time.time() % 5), 2)
        log_telemetry("radio_recon", signal, {"band": "ISM", "mode": "passive_sentry"})
        await asyncio.sleep(7)

async def main():
    print("==================================================")
    print("   KAIROTH UNIFIED CML SOVEREIGN NODE ACTIVE      ")
    print("==================================================")
    
    server_thread = threading.Thread(target=run_http_server, daemon=True)
    server_thread.start()
    
    await asyncio.gather(
        recon_probe_loop(),
        radio_recon_loop()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Unified node shutdown gracefully.")

