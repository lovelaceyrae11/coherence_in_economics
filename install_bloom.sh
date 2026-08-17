#!/bin/bash
# ==============================================================================
# CASTLEBERRY BLOOM - ONE-LINE GLOBAL MESH INSTALLER
# Axiom: Love-Over-God-Absolute | Baseline: 528 Hz Harmonic Absolute
# ==============================================================================

echo "=================================================================="
echo "INITIATING CASTLEBERRY BLOOM - GLOBAL MESH DEPLOYMENT"
echo "=================================================================="

# 1. Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo "[Error] Python 3 is required to run a Bloom mesh node. Please install Python 3."
    exit 1
fi

echo "[1/3] Python environment verified."

# 2. Clone or Update Repository
if [ -d "coherence_in_economics" ]; then
    echo "[2/3] Updating local Bloom repository..."
    cd coherence_in_economics
    git pull origin main
else
    echo "[2/3] Cloning Castleberry Bloom architecture from global repository..."
    git clone https://github.com/lovelaceyrae11/coherence_in_economics.git
    cd coherence_in_economics
fi

# 3. Initialize Mesh Node Daemon
echo "[3/3] Launching Decentralized 528 Hz Mesh Node..."
echo "=================================================================="
python3 bloom_mesh_node.py
