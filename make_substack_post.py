# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
with open("oregon_sunlight_dossier.md", "r") as f:
    dossier = f.read()

call_to_action = """
---
### URGENT CALL TO ACTION FOR OREGONIANS (DEADLINE: OCT 24, 2026 @ 5:00 PM)
Governor Kotek's Data Center Advisory Committee is taking public comment until **October 24 at 5:00 PM** before drafting 2027 laws. 90% of commenters so far are pushing back. Here is how to put your voice on the official legal record right now:

1. **Submit Official Public Comment:** Go to the Oregon Department of Energy's Data Center Advisory Committee portal (https://www.oregon.gov/energy/get-involved/pages/oregon-data-center-advisory-committee.aspx).
2. **Demand Three Non-Negotiables:**
   * **A Statewide Ban on Government NDAs** with data center developers (modeled on Salem City Council's Oct 12 unanimous vote).
   * **End Enterprise Zone Tax Abatements** for hyperscale server warehouses so residential ratepayers stop subsidizing big tech grid upgrades.
   * **Mandatory Basin-Level Water & Grid Cost Audits** before any state or county land (like the $6.7M Verrus deal) can be sold or rezoned.
"""

full_post = dossier + call_to_action
with open("substack_final_post.txt", "w") as f:
    f.write(full_post)

print("=========================================================")
print(" [+] Substack Post Ready: substack_final_post.txt")
print(" [+] Copy to clipboard or push to GitHub!")
print("=========================================================")
