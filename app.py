import psutil
import time

print("="*50)
print(" 🚀 DevOps Automated Server & Disk Health Monitor")
print("="*50)

# System Metrics
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print(f"📊 CPU Usage    : {cpu}%")
print(f"💾 RAM Usage    : {memory}%")
print(f"💽 Disk Usage   : {disk}%")

# DevOps Alert Simulation
if cpu > 80 or memory > 80 or disk > 80:
    print("⚠️  WARNING: High Resource Usage Detected! Triggering Alert...")
else:
    print("✅ STATUS: All System Metrics are Normal & Healthy.")

print("="*50)
print("Automation Script Executed Successfully via DevOps Pipeline!")