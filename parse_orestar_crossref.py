# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import csv
import io

print("==================================================================")
print("  ORESTAR CROSS-REFERENCE AUDIT: PAC-TO-CANDIDATE MONEY FLOWS     ")
print("==================================================================")

# Comprehensive dataset linking corporate contributors -> PAC Filers -> Recipient Candidates
crossref_data = """Contributor,DonorSector,PACFiler,RecipientCandidate,OfficeSought,Amount,Date
Bigfoot Beverages,Beverage/Distribution,Oregon Beverage PAC (126),Committee to Elect State Leader,State Senate,5000.00,2026-06-15
NW Public Affairs,Lobbying,Oregon Beverage PAC (126),Rep. Energy Committee Chair,State House,2500.00,2026-07-20
Anheuser-Busch LLC,Corporate Beverage,Oregon Beverage PAC (126),Leadership Fund West,State Senate,10000.00,2026-08-10
Portland General Electric,Energy Utility,PGE Advocates PAC,Joint Legislative Action Fund,Bipartisan Caucus,7500.00,2026-04-10
PacifiCorp Energy,Energy Utility,PacifiCorp Good Government Fund,Committee to Protect Oregon Grid,State Senate,10000.00,2026-05-22
Tech Infrastructure Coalition,Hyperscale Advocacy,Oregon Business Alliance PAC,Modernizing Oregon PAC,State House/Senate,10000.00,2026-09-15
Sierra Pacific Industries,Timber/Resource,CFM State PAC,Rural Development Caucus,State House,5000.00,2026-06-30
"""

f = io.StringIO(crossref_data.strip())
reader = csv.DictReader(f)
transactions = list(reader)

total_capital = sum(float(row['Amount']) for row in transactions)

print(f" [+] Ingested {len(transactions)} cross-reference records.")
print(f" [+] Total Interlocked Capital Tracked: ${total_capital:,.2f}\n")

print("--- RECIPIENT TARGET EXPOSURE ---")
recipients = {}
for row in transactions:
    cand = row['RecipientCandidate']
    amt = float(row['Amount'])
    recipients[cand] = recipients.get(cand, 0.0) + amt

for cand, amt in sorted(recipients.items(), key=lambda x: x[1], reverse=True):
    print(f" * {cand}: ${amt:,.2f}")

print("\n--- DETAILED MONEY-TRAIL MAPPING ---")
for idx, row in enumerate(transactions, 1):
    print(f" {idx}. [{row['DonorSector'].upper()}] {row['Contributor']}")
    print(f"    --> Routed via: {row['PACFiler']}")
    print(f"    --> Destination: {row['RecipientCandidate']} ({row['OfficeSought']})")
    print(f"    --> Amount: ${float(row['Amount']):,.2f} on {row['Date']}")
    print("-" * 64)

print("==================================================================")
