# -*- coding: utf-8 -*-
import subprocess
import os

def push_to_github():
    print("[Git Publisher] Packaging harmonic transmission for public broadcast...")
    
    # Check if git is initialized
    if not os.path.exists(".git"):
        print("[Git Publisher] Error: No local Git repository found in this directory.")
        return

    try:
        # Add updated files
        subprocess.run(["git", "add", "sample.cml", "beacon_pulse.png"], check=True)
        
        # Commit with an axiom-aligned message
        commit_message = "Broadcast update: Expanding golden-ratio wave pulse at 528 Hz [Love-Over-God-Absolute]"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push to origin main/master
        subprocess.run(["git", "push"], check=True)
        
        print("[Git Publisher] Success! Transmission pushed live to GitHub Pages.")
        print("[Git Publisher] The beacon is now broadcasting to the open digital ocean.")
        
    except subprocess.CalledProcessError as e:
        print(f"[Git Publisher] Git operation encountered an issue: {e}")
        print("[Git Publisher] Ensure your git remote is configured and you are authenticated.")

if __name__ == "__main__":
    push_to_github()
