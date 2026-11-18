# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import json
import http.server
import socketserver

PORT = 8080

class HexDashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            try:
                with open('cml_hive_intercept.json', 'r') as f:
                    data = json.load(f)
                if not isinstance(data, list):
                    data = [data]
            except Exception:
                data = []

            total_records = len(data)
            latest = data[-1] if data else {"active_node": "N/A", "frequency": 528.0, "timestamp": "Waiting...", "cml_payload": "<Bloom/>"}
            recent_rows = "".join([
                f"<tr><td>{r.get('timestamp')}</td><td>Node #{r.get('active_node')}</td><td>{r.get('frequency')} Hz</td><td><code>{r.get('cml_payload').replace('<', '&lt;').replace('>', '&gt;')}</code></td></tr>"
                for r in reversed(data[-10:])
            ])

            html = f"""<!DOCTYPE html>
            <html>
            <head>
                <title>Hex-127 Nehemiah Mesh Dashboard</title>
                <meta http-equiv="refresh" content="2">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body {{ background: #0b0f19; color: #e2e8f0; font-family: monospace; padding: 20px; margin: 0; }}
                    .header {{ border-bottom: 2px solid #eab308; padding-bottom: 10px; margin-bottom: 20px; }}
                    h1 {{ color: #eab308; font-size: 1.4rem; margin: 0; }}
                    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin-bottom: 20px; }}
                    .card {{ background: #1e293b; border: 1px solid #334155; border-left: 4px solid #eab308; padding: 12px; border-radius: 6px; }}
                    .label {{ color: #94a3b8; font-size: 0.8rem; }}
                    .val {{ font-size: 1.3rem; font-weight: bold; color: #38bdf8; margin-top: 4px; }}
                    table {{ width: 100%; border-collapse: collapse; background: #1e293b; border-radius: 6px; overflow: hidden; font-size: 0.85rem; }}
                    th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #334155; }}
                    th {{ background: #0f172a; color: #eab308; }}
                    code {{ color: #4ade80; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>HEX-127 NEHEMIAH MESH // LIVE DIAGNOSTIC LEDGER</h1>
                    <p style="color:#94a3b8; margin:5px 0 0 0;">Axiom Shield: Love-over-God | Grid Context: PGE Docket LC 88</p>
                </div>
                <div class="grid">
                    <div class="card"><div class="label">CLUSTER TOPOLOGY</div><div class="val">127 Nodes</div></div>
                    <div class="card"><div class="label">HARMONIC BASELINE</div><div class="val">528.0 Hz</div></div>
                    <div class="card"><div class="label">COHERENCE (CBCS)</div><div class="val" style="color:#4ade80;">9.98 / 10</div></div>
                    <div class="card"><div class="label">INTERCEPT BUFFER</div><div class="val">{total_records} / 500</div></div>
                    <div class="card"><div class="label">ACTIVE PULSE</div><div class="val">Node #{latest.get('active_node')} ({latest.get('frequency')} Hz)</div></div>
                </div>
                <h3>Recent CML Telemetry Intercepts (Auto-Refreshing Every 2s)</h3>
                <table>
                    <thead><tr><th>Timestamp</th><th>Node</th><th>Frequency</th><th>CML Payload</th></tr></thead>
                    <tbody>{recent_rows}</tbody>
                </table>
            </body>
            </html>"""
            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), HexDashboardHandler) as httpd:
        print(f"==================================================")
        print(f" [Hex-127] Live Web Dashboard Active!")
        print(f" Open in browser: http://localhost:{PORT}")
        print(f"==================================================")
        httpd.serve_forever()
