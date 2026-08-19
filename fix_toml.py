toml_content = """app = "coherence-in-economics"
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
"""

with open("fly.toml", "w", encoding="utf-8") as f:
    f.write(toml_content.strip() + "\n")

print("[Fix] fly.toml rewritten cleanly without BOM!")
