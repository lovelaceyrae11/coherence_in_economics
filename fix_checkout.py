with open(".github/workflows/fly.yml", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("actions/checkout@v4", "actions/checkout@v5")

with open(".github/workflows/fly.yml", "w", encoding="utf-8") as f:
    f.write(content)

print("[Fix] Updated actions/checkout to v5!")
