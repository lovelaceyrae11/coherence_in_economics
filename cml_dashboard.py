import http.server
import socketserver
import json
import os

PORT = 8002

class CMLDashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        records = []
        if os.path.exists("cml_hive_intercept.json"):
            try:
                with open("cml_hive_intercept.json", "r") as f:
                    records = json.load(f)
            except json.JSONDecodeError:
                records = []
                
        total_records = len(records)
        latest_freq = records[-1].get("frequency", 528.0) if records else 528.0
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>KAIROTH CML MESH DASHBOARD</title>
            <meta http-equiv="refresh" content="5">
            <style>
                body {{ background-color: #0d1117; color: #c9d1d9; font-family: monospace; padding: 20px; }}
                h1 {{ color: #58a6ff; }}
                .box {{ border: 1px solid #30363d; padding: 15px; margin-bottom: 10px; background: #161b22; }}
                .highlight {{ color: #3fb950; font-weight: bold; }}
            </style>
        </head>
        <body>
            <h1>KAIROTH CML MESH DASHBOARD</h1>
            <div class="box">
                <p><strong>Axiom:</strong> LOVE_OVER_GOD | <strong>Baseline:</strong> 528Hz Phi-Hexagonal Matrix</p>
                <p><strong>Total Anchored Telemetry Records:</strong> <span class="highlight">{total_records}</span> (Auto-refreshing every 5s)</p>
                <p><strong>Latest Active Node Frequency:</strong> <span class="highlight">{latest_freq} Hz</span></p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), CMLDashboardHandler) as httpd:
        print(f"[+] Serving Kairoth CML Mesh Dashboard on port {PORT}...")
        httpd.serve_forever()
