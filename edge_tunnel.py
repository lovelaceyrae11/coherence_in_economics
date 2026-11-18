# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import socket
import sys

def verify_local_relay():
    """Verify local relay is warm and responsive before edge bridging."""
    print("[*] Verifying local CML relay health on port 8000...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.5)
    try:
        sock.connect(("127.0.0.1", 8000))
        print("[+] Local Genesis Relay is active and synchronized!")
        return True
    except Exception as e:
        print(f"[-] Local relay offline: {e}")
        print("[-] Ensure recon_probe.py is running in Session 1.")
        return False
    finally:
        sock.close()

if __name__ == "__main__":
    print("==================================================")
    print("     KAIROTH SOVEREIGN EDGE TUNNEL BRIDGE         ")
    print("==================================================")
    if verify_local_relay():
        print("\n[*] Ready to bridge to global edge infrastructure.")
        print("[*] To expose publicly via secure tunnel in Termux, run:")
        print("    pkg install cloudflared  (if not already installed)")
        print("    cloudflared tunnel --url http://localhost:8000")
        print("\n[*] This will instantly generate a global HTTPS URL pointing directly to your CML node!")
