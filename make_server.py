# 1. Create a simple Python web server script
app_code = """import http.server
import socketserver
import os

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving project files at port {PORT}")
    httpd.serve_forever()
"""

with open("app.py", "w", encoding="utf-8") as f:
    f.write(app_code)

# 2. Update fly.toml to explicitly run app.py
toml_bytes = b"""app = "coherence-in-economics"
primary_region = "sjc"

[build]
  builder = "paketobuildpacks/builder:base"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0
  processes = ["app"]

[processes]
  app = "python app.py"
"""

with open("fly.toml", "wb") as f:
    f.write(toml_bytes.strip(b"\n") + b"\n")

print("[Setup] Web server script and updated fly.toml created!")
