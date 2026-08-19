import os

# 1. Write clean binary fly.toml (Zero BOM guaranteed)
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
"""
with open("fly.toml", "wb") as f:
    f.write(toml_bytes.strip(b"\n") + b"\n")

# 2. Write clean workflow file (Bypassing wrapper action)
os.makedirs(".github/workflows", exist_ok=True)
workflow_content = """name: Fly Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    name: Deploy app
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install Flyctl
        run: |
          curl -L https://fly.io/install.sh | sh
          echo "$HOME/.fly/bin" >> $GITHUB_PATH

      - name: Deploy to Fly
        run: |
          ~/.fly/bin/flyctl deploy --remote-only
        env:
          FLY_API_TOKEN: ${{ secrets.FLY_API_TOKEN }}
"""
with open(".github/workflows/fly.yml", "w", encoding="utf-8") as f:
    f.write(workflow_content)

print("[Setup] Both fly.toml (binary) and fly.yml (direct curl) generated successfully!")
