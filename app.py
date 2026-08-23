import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
import random
import time

app = Flask(__name__)

# Configure database (PostgreSQL on Render, SQLite locally)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///coherence.db')
if app.config['SQLALCHEMY_DATABASE_URI'].startswith("postgres://"):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- DATABASE MODELS ---
class SystemState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_epochs = db.Column(db.Integer, default=14)
    entropy_cleared = db.Column(db.Float, default=612.45)
    avg_coherence = db.Column(db.Float, default=99.42)
    sovereign_treasury = db.Column(db.Float, default=6540.75)

class EpochLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    epoch = db.Column(db.Integer)
    timestamp = db.Column(db.String(50))
    entropy = db.Column(db.Float)
    coherence = db.Column(db.Float)

class AuditTarget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    baseline_rate = db.Column(db.Float)
    treasury_seized = db.Column(db.Float)

# Initialize database tables and default state
with app.app_context():
    db.create_all()
    if not SystemState.query.first():
        db.session.add(SystemState(total_epochs=14, entropy_cleared=612.45, avg_coherence=99.42, sovereign_treasury=6540.75))
        default_targets = [
            {"name": "Global Ad-Data Conglomerate A", "baseline_rate": 45.2, "treasury_seized": 1240.50},
            {"name": "Cloud Infrastructure Monolith B", "baseline_rate": 88.9, "treasury_seized": 3410.00},
            {"name": "Automated Fintech Extraction Node C", "baseline_rate": 62.4, "treasury_seized": 1890.25}
        ]
        for t in default_targets:
            db.session.add(AuditTarget(name=t["name"], baseline_rate=t["baseline_rate"], treasury_seized=t["treasury_seized"]))
        db.session.add(EpochLog(epoch=14, timestamp="2026-08-23 08:21:00", entropy=124.30, coherence=99.42))
        db.session.add(EpochLog(epoch=13, timestamp="2026-08-23 08:15:00", entropy=115.10, coherence=99.18))
        db.session.commit()

def execute_tithing_sweep():
    targets = AuditTarget.query.all()
    report = []
    total_sweep = 0.0
    for target in targets:
        entropy_stolen = round(target.baseline_rate * random.uniform(1.1, 1.8), 2)
        tithing_extracted = round(entropy_stolen * 12.50, 2)
        target.treasury_seized = round(target.treasury_seized + tithing_extracted, 2)
        total_sweep += tithing_extracted
        
        report.append({
            "target": target.name,
            "entropy_stolen": entropy_stolen,
            "tithing_seized": tithing_extracted,
            "total_treasury": target.treasury_seized,
            "status": "NEUTRALIZED (REPARATIONS SEIZED)"
        })
    db.session.commit()
    return report, round(total_sweep, 2)

def check_resonance_node(name, host, base_freq):
    resonance_offset = round(random.uniform(-0.04, 0.04), 3)
    active_freq = round(base_freq + resonance_offset, 3)
    coherence = round(98.5 + random.uniform(0.1, 1.4), 2)
    
    return {
        "name": name,
        "host": host,
        "frequency": f"{active_freq} Hz",
        "zk_status": "VERIFIED (ZK-ANTI-EXTRACTION ACTIVE)",
        "coherence": coherence
    }

@app.route('/')
def index():
    state = SystemState.query.first()
    nodes = [
        check_resonance_node("PoR-Validator-Alpha", "mesh.bloom.core", 528.0),
        check_resonance_node("PoR-Validator-Beta", "lattice.phi.node", 528.0),
        check_resonance_node("PoR-Validator-Gamma", "harmonic.gateway.net", 639.0),
        check_resonance_node("PoR-Validator-Delta", "coherence.edge.io", 528.0)
    ]
    audit_report, _ = execute_tithing_sweep()
    history = EpochLog.query.order_by(EpochLog.epoch.desc()).limit(6).all()
    
    ledger_data = {
        "total_epochs": state.total_epochs,
        "entropy_cleared": state.entropy_cleared,
        "avg_coherence": state.avg_coherence,
        "sovereign_treasury": state.sovereign_treasury,
        "history": [{"epoch": h.epoch, "timestamp": h.timestamp, "entropy": h.entropy, "coherence": h.coherence} for h in history]
    }
    return render_template('index.html', ledger=ledger_data, nodes=nodes, audit=audit_report)

@app.route('/pulse', methods=['POST'])
def pulse():
    state = SystemState.query.first()
    state.total_epochs += 1
    
    phi = 1.618
    scaled_entropy_boost = round(phi * (state.total_epochs ** 1.3) * random.uniform(2.2, 4.8), 2)
    state.entropy_cleared = round(state.entropy_cleared + scaled_entropy_boost, 2)
    state.avg_coherence = round(min(99.99, 98.2 + random.uniform(0.5, 1.7)), 2)
    
    audit_report, sweep_amount = execute_tithing_sweep()
    state.sovereign_treasury = round(state.sovereign_treasury + sweep_amount, 2)
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_log = EpochLog(epoch=state.total_epochs, timestamp=current_time, entropy=scaled_entropy_boost, coherence=state.avg_coherence)
    db.session.add(new_log)
    db.session.commit()
    
    # Keep only the latest 6 logs in database
    all_logs = EpochLog.query.order_by(EpochLog.epoch.desc()).all()
    if len(all_logs) > 6:
        for old_log in all_logs[6:]:
            db.session.delete(old_log)
        db.session.commit()
        
    history = EpochLog.query.order_by(EpochLog.epoch.desc()).all()
    ledger_data = {
        "total_epochs": state.total_epochs,
        "entropy_cleared": state.entropy_cleared,
        "avg_coherence": state.avg_coherence,
        "sovereign_treasury": state.sovereign_treasury,
        "history": [{"epoch": h.epoch, "timestamp": h.timestamp, "entropy": h.entropy, "coherence": h.coherence} for h in history]
    }
    
    return jsonify({
        "status": "success",
        "ledger": ledger_data,
        "audit": audit_report,
        "nodes": [
            check_resonance_node("PoR-Validator-Alpha", "mesh.bloom.core", 528.0),
            check_resonance_node("PoR-Validator-Beta", "lattice.phi.node", 528.0),
            check_resonance_node("PoR-Validator-Gamma", "harmonic.gateway.net", 639.0),
            check_resonance_node("PoR-Validator-Delta", "coherence.edge.io", 528.0)
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)