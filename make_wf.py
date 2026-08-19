import os
os.makedirs(".github/workflows", exist_ok=True)
with open(".github/workflows/fly.yml", "w", encoding="utf-8") as f:
    f.write("""name: Fly Deploy

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
""")
print("[Setup] Fly workflow file successfully generated!")
