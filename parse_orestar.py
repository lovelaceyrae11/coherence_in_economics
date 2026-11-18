# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import csv
import io
import os
import sys

print("=========================================================")
print("   ADVANCED OREGON ORESTAR CAMPAIGN FINANCE AUDIT ENGINE   ")
print("=========================================================")

# Default mock dataset simulating bulk ORESTAR extracts for targeted PACs 
# (Easily replaceable by saving a real ORESTAR CSV export as 'orestar_export.csv')
default_csv_data = """Filer,Contributor,Amount,Category,Date,City
Oregon Beverage PAC (126),Bigfoot Beverages,5000.00,Beverage/Distribution,2026-06-15,Eugene
Oregon Beverage PAC (126),NW Public Affairs,2500.00,Lobbying,2026-07-20,Salem
Oregon Beverage PAC (126),Anheuser-Busch LLC,10000.00,Corporate Beverage,2026-08-10,St. Louis
Oregon Beverage PAC (126),Columbia Distributing,7500.00,Beverage Distribution,2026-09-01,Portland
Jobs PAC,Altria Client Services,2500.00,Industrial/Tobacco,2026-05-12,Richmond
CFM State PAC,Sierra Pacific Industries,5000.00,Timber/Resource,2026-06-30,Anderson
Oregon Business Alliance PAC,Tech Infrastructure Coalition,10000.00,Hyperscale Advocacy,2026-09-15,Portland
PGE Advocates PAC,Portland General Electric,7500.00,Energy Utility,2026-04-10,Portland
PacifiCorp Good Government Fund,PacifiCorp Energy,10000.00,Energy Utility,2026-05-22,Portland
"""

target_file = "orestar_export.csv"

if os.path.exists(target_file):
    print(f" [+] Found local file '{target_file}'. Loading data...")
    with open(target_file, "r", encoding="utf-8") as f:
        file_content = f.read()
else:
    print(f" [!] '{target_file}' not found. Using structured simulation payload.")
    print(f"     (Tip: Drop any ORESTAR CSV export into this folder as '{target_file}' to parse real data)\n")
    file_content = default_csv_data.strip()

f = io.StringIO(file_content)
reader = csv.DictReader(f)

transactions = list(reader)
total_capital = sum(float(row['Amount']) for row in transactions)

# Interactive Category Filter Prompt or default full sweep
print(f" [+] Successfully ingested {len(transactions)} transaction nodes.")
print(f" [+] Total Tracked Capital Pool: ${total_capital:,.2f}\n")

print("--- SECTOR BREAKDOWN ANALYSIS ---")
sectors = {}
for row in transactions:
    cat = row['Category']
    amt = float(row['Amount'])
    sectors[cat] = sectors.get(cat, 0.0) + amt

for cat, amt in sorted(sectors.items(), key=lambda x: x[1], reverse=True):
    pct = (amt / total_capital) * 100
    print(f" * {cat}: ${amt:,.2f} ({pct:.1f}%)")

print("\n--- DETAILED TRANSACTION LOG ---")
for idx, row in enumerate(transactions, 1):
    print(f" {idx}. Filer: {row['Filer']}")
    print(f"    -> Contributor: {row['Contributor']} ({row['City']})")
    print(f"    -> Amount: ${float(row['Amount']):,.2f} | Category: {row['Category']} | Date: {row['Date']}")
    print("-" * 60)

print("=========================================================")
