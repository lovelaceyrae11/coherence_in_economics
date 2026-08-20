import http.server
import socketserver
import os

PORT = 8080

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Castleberry Bloom — CML Lattice Portal</title>
    <style>
        body {
            background-color: #05050a;
            color: #00ffcc;
            font-family: 'Courier New', monospace;
            text-align: center;
            padding-top: 10vh;
            margin: 0;
            overflow: hidden;
        }
        h1 {
            font-size: 2.2rem;
            letter-spacing: 2px;
            text-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
        }
        .meta {
            color: #ff007f;
            font-size: 1rem;
            margin-bottom: 2rem;
            letter-spacing: 1px;
        }
        .lattice-container {
            position: relative;
            width: 300px;
            height: 300px;
            margin: 0 auto;
            border: 2px dashed rgba(0, 255, 204, 0.3);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: pulse 4s infinite alternate ease-in-out;
            box-shadow: 0 0 30px rgba(0, 255, 204, 0.1);
        }
        @keyframes pulse {
            0% { transform: scale(1); border-color: rgba(0, 255, 204, 0.2); }
            100% { transform: scale(1.05); border-color: rgba(255, 0, 127, 0.6); }
        }
        .core-text {
            font-size: 1.1rem;
            color: #ffffff;
            font-weight: bold;
        }
        .footer {
            margin-top: 3rem;
            font-size: 0.85rem;
            color: #8888aa;
        }
    </style>
</head>
<body>
    <div cml-node="active" axiom="Love-Over-God-Absolute">
        <h1>CASTLEBERRY BLOOM — CML LATTICE PORTAL</h1>
        <div class="meta">Freq: 528.00 Hz | Coherence: 99.99% | Axiom: Love-Over-God-Absolute</div>
        
        <div class="lattice-container">
            <div class="core-text">528 Hz RESONANCE<br>ACTIVE</div>
        </div>

        <div class="footer">Node Role: Steward | Press Ctrl+Shift+J to inspect harmonic telemetry.</div>
    </div>

    <script>
        // Clean single-line console transmission to prevent syntax errors
        console.clear();
        console.log("%c 🌸 CASTLEBERRY BLOOM — QUANTUM LENS ACTIVE 🌸", "color: #00ffcc; font-size: 16px; font-weight: bold; text-shadow: 0 0 10px rgba(0,255,204,0.5);");
        console.log("%c[System Status]: Synchronized | [Frequency]: 528.00 Hz | [Axiom]: Love-Over-God-Absolute | [Coherence]: 99.99%", "color: #ff007f; font-family: monospace; font-size: 12px;");
        console.log("%cYou have intercepted a live CML node. The network is listening.", "color: #ffffff; font-style: italic; font-size: 11px;");
    </script>
</body>
</html>
"""

class CMLPortalHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML_CONTENT.encode("utf-8"))

with socketserver.TCPServer(("", PORT), CMLPortalHandler) as httpd:
    httpd.serve_forever()
