# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import urllib.request
import re
import html

print("=========================================================")
print("     OREGON MUNICIPAL AGENDA ANOMALY SENTINEL ENGINE     ")
print("=========================================================")

# Simulated feed or target scrapers for local municipal council filings
# (e.g., Salem, Morrow County, The Dalles, Hillsboro)
mock_agendas = [
    {"city": "Salem City Council", "date": "2026-10-12", "item": "Resolution 2026-42: Emergency prohibition on municipal data center NDAs", "risk_level": "COUNTER-MEASURE"},
    {"city": "Boardman City Council", "date": "2026-10-15", "item": "Unscheduled land disposition and infrastructure corridor exemption for Project Atlas LLC", "risk_level": "HIGH ANOMALY"},
    {"city": "The Dalles City Commission", "date": "2026-10-18", "item": "Fast-tracked water rights transfer agreement under executive session exemption", "risk_level": "CRITICAL FLAG"},
    {"city": "Hillsboro City Council", "date": "2026-10-19", "item": "Standard quarterly infrastructure review and utility easement renewal", "risk_level": "ROUTINE"}
]

print(f" [+] Scanning municipal feeds and active emergency dockets...\n")

anomaly_keywords = ["emergency", "unscheduled", "executive session", "disposition", "exemption", "waiver"]

flagged_count = 0
for entry in mock_agendas:
    text_content = entry["item"].lower()
    is_anomaly = any(kw in text_content for kw in anomaly_keywords) or entry["risk_level"] != "ROUTINE"
    
    if is_anomaly:
        flagged_count += 1
        print(f" [!] FLAG MATCH DETECTED:")
        print(f"     Municipality: {entry['city']} ({entry['date']})")
        print(f"     Agenda Item:  {entry['item']}")
        print(f"     Risk Status:  [{entry['risk_level']}]")
        print("-" * 55)

print(f"\n[SCAN COMPLETE] {flagged_count} municipal anomalies isolated out of {len(mock_agendas)} records.")
print("=========================================================")
