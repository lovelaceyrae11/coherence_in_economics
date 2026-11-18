# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import urllib.request
import re
import html

print("=========================================================")
print("   GLASTONBURY & NEW ENGLAND AI / GRID WATCHDOG SCANNER   ")
print("=========================================================")

url = "https://news.google.com/rss/search?q=Glastonbury+Connecticut+%22data+center%22+OR+%22ArcLight%22+OR+%22DigitalBridge%22+OR+%22ISO-NE%22&hl=en-US&gl=US&ceid=US:en"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    xml = urllib.request.urlopen(req, timeout=10).read().decode("utf-8")
    titles = re.findall(r"<title>(.*?)</title>", xml)[2:10]

    for i, t in enumerate(titles, 1):
        clean_title = html.unescape(t)
        print(f" {i}. {clean_title}")
except Exception as e:
    print(f"    [!] Watchdog Feed Error: {e}")

print("=========================================================")
