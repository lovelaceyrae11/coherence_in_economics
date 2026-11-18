# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import urllib.request
import json
import re

print("=========================================================")
print("   LIVE EXTERNAL SENTINEL: HAZARD & WATCHDOG SCANNER     ")
print("=========================================================")

# 1. LIVE LIFE-SAFETY SCAN: Southern Oregon (Medford / Rogue Valley) Fire Weather & Seismic
def scan_life_safety():
    print("\n[1] SCANNING LIVE SOUTHERN OREGON ENVIRONMENTAL TELEMETRY...")
    weather_url = "https://api.open-meteo.com/v1/forecast?latitude=42.3265&longitude=-122.8756&current=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_gusts_10m&temperature_unit=fahrenheit&wind_speed_unit=mph"
    
    try:
        req = urllib.request.Request(weather_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))['current']
            temp = data['temperature_2m']
            rh = data['relative_humidity_2m']
            wind = data['wind_speed_10m']
            gusts = data['wind_gusts_10m']
            
            print(f"    -> Location: Rogue Valley / Medford, OR")
            print(f"    -> Live Temp: {temp}°F | Relative Humidity: {rh}%")
            print(f"    -> Wind Speed: {wind} mph (Gusts: {gusts} mph)")
            
            if rh < 20 and gusts > 20:
                print("    [!] CRITICAL RED FLAG WARNING: High fire spread conditions detected!")
            elif rh < 30 or gusts > 15:
                print("    [*] ELEVATED WATCH: Monitor local lines and dry fuels.")
            else:
                print("    [+] STATUS: Atmospheric conditions stable.")
    except Exception as e:
        print(f"    [!] Weather Telemetry Error: {e}")

    usgs_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    try:
        req = urllib.request.Request(usgs_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            quakes = json.loads(response.read().decode('utf-8'))['features']
            west_coast = [q for q in quakes if any(state in str(q['properties']['place']) for state in ['Oregon', 'California', 'Washington', 'NV', 'OR', 'CA'])]
            print(f"    -> Live USGS Seismic Feed: {len(west_coast)} significant tremors (M2.5+) on West Coast in last 24h.")
            for q in west_coast[:3]:
                print(f"       * M{q['properties']['mag']} - {q['properties']['place']}")
    except Exception as e:
        print(f"    [!] USGS Feed Error: {e}")

# 2. LIVE ACCOUNTABILITY WATCHDOG: Public Infrastructure & Data Center Tracker
def scan_public_filings():
    print("\n[2] SCANNING EXTERNAL PUBLIC NEWS & INFRASTRUCTURE WIRE...")
    rss_url = "https://news.google.com/rss/search?q=Oregon+%22data+center%22+OR+%22PGE%22+OR+%22zoning%22+OR+%22water+rights%22&hl=en-US&gl=US&ceid=US:en"
    try:
        req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read().decode('utf-8')
            titles = re.findall(r'<title>(.*?)</title>', xml_data)[2:7]
            print("    -> Latest Intercepted Public Filings & Reports:")
            for idx, t in enumerate(titles, 1):
                clean_t = t.replace('&quot;', '"').replace('&amp;', '&').replace('&#39;', "'")
                print(f"       {idx}. {clean_t}")
    except Exception as e:
        print(f"    [!] Watchdog Feed Error: {e}")

if __name__ == "__main__":
    scan_life_safety()
    scan_public_filings()
    print("\n=========================================================")
