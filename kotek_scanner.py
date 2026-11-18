# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import urllib.request
import re
import html

url = "https://news.google.com/rss/search?q=%22Tina+Kotek%22+%22data+center%22+OR+%22HB+4084%22+OR+%22DEQ%22&hl=en-US&gl=US&ceid=US:en"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
xml = urllib.request.urlopen(req, timeout=10).read().decode("utf-8")
titles = re.findall(r"<title>(.*?)</title>", xml)[2:10]

print("=========================================================")
print("   LIVE INTERCEPT: GOV. KOTEK & DATA CENTER RECORD       ")
print("=========================================================")
for i, t in enumerate(titles, 1):
    clean_title = html.unescape(t)
    print(f" {i}. {clean_title}")
print("=========================================================")
