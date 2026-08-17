import psutil
import time

def get_real_hardware_telemetry():
    """
    Pulls live hardware telemetry from the host machine's actual sensors.
    """
    print("[Hardware-Bridge] Interfacing with physical system sensors...")
    
    # Get actual CPU utilization percentage
    cpu_load = psutil.cpu_percent(interval=1)
    
    # Get actual CPU frequency
    cpu_freq = psutil.cpu_freq()
    current_freq = cpu_freq.current if cpu_freq else 2500.0
    
    # Attempt to read true physical thermal sensors (supported natively on Linux/macOS, 
    # and some Windows configurations with administrator permissions)
    temps = {}
    try:
        if hasattr(psutil, "sensors_temperatures"):
            temps = psutil.sensors_temperatures()
    except Exception as e:
        temps = {"note": "OS restricted direct thermal diode access"}

    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_load_percent": cpu_load,
        "cpu_current_freq_mhz": current_freq,
        "raw_thermal_sensors": temps
    }

if __name__ == "__main__":
    print("======================================================")
    print("CASTLEBERRY BLOOM - LIVE HARDWARE TELEMETRY BRIDGE")
    print("======================================================")
    
    telemetry = get_real_hardware_telemetry()
    
    print(f"Timestamp:          {telemetry['timestamp']}")
    print(f"Live CPU Load:      {telemetry['cpu_load_percent']}%")
    print(f"Live CPU Frequency: {telemetry['cpu_current_freq_mhz']} MHz")
    print(f"Sensor Readings:    {telemetry['raw_thermal_sensors']}")
    print("======================================================")
    print("Hardware bridge active. Ready to bind to the Bloom engine.")