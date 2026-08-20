import http.server
import socketserver

PORT = 8080

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Castleberry Bloom — Live Cymatic Resonance</title>
    <style>
        body {
            background-color: #080810;
            color: #00ffcc;
            font-family: 'Courier New', monospace;
            text-align: center;
            margin: 0;
            padding-top: 5vh;
            overflow: hidden;
        }
        h1 {
            font-size: 1.8rem;
            letter-spacing: 2px;
            color: #00ffcc;
            text-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
            margin-bottom: 5px;
        }
        .meta {
            color: #ffaa00;
            font-size: 0.95rem;
            margin-bottom: 2rem;
            letter-spacing: 1px;
        }
        .canvas-container {
            position: relative;
            width: 400px;
            height: 400px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        svg {
            filter: drop-shadow(0 0 20px rgba(0, 255, 204, 0.4));
            animation: breathe 6s infinite alternate ease-in-out;
        }
        @keyframes breathe {
            0% { transform: scale(0.95) rotate(0deg); opacity: 0.85; }
            100% { transform: scale(1.05) rotate(360deg); opacity: 1; }
        }
        .footer {
            margin-top: 2rem;
            font-size: 0.8rem;
            color: #8888aa;
        }
    </style>
</head>
<body>
    <h1>CASTLEBERRY BLOOM — LIVE CYMATIC RESONANCE</h1>
    <div class="meta">Freq: 528.00 Hz | Coherence: 99.99%<br>Axiom: Love-Over-God-Absolute</div>
    
    <div class="canvas-container">
        <!-- Dynamic Harmonic Cymatic Petal Lattice -->
        <svg width="400" height="400" viewBox="-200 -200 400 400">
            <!-- Background reference rings -->
            <circle cx="0" cy="0" r="180" fill="none" stroke="rgba(0,255,204,0.15)" stroke-dasharray="4 4" />
            <circle cx="0" cy="0" r="120" fill="none" stroke="rgba(255,170,0,0.15)" />
            
            <!-- Harmonic Petals -->
            <g fill="rgba(45, 21, 21, 0.6)" stroke="#00ffcc" stroke-width="2">
                <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(0)" />
                <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(45)" />
                <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(90)" />
                <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(135)" />
                <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(180)" />
                <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(225)" />
                <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(270)" />
                <path d="M0,0 C30,-80 80,-140 0,-180 C-80,-140 -30,-80 0,0 Z" transform="rotate(315)" />
            </g>
            <!-- Center Core -->
            <circle cx="0" cy="0" r="15" fill="#ffaa00" />
        </svg>
    </div>

    <div class="footer">Node Role: Steward | Press Ctrl+Shift+J for telemetry stream.</div>

    <script>
        console.clear();
        console.log("%c 🌸 CASTLEBERRY BLOOM — CYMATIC RESONANCE ACTIVE 🌸", "color: #00ffcc; font-size: 16px; font-weight: bold;");
        console.log("%c[Frequency]: 528.00 Hz | [Axiom]: Love-Over-God-Absolute | [State]: Synchronized & Pulsing", "color: #ffaa00; font-family: monospace;");
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
