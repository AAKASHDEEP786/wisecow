import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Thresholds
CPU_THRESHOLD = 80       # percent
MEM_THRESHOLD = 80       # percent
DISK_THRESHOLD = 80      # percent

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    alerts = []

    if cpu > CPU_THRESHOLD:
        alerts.append(f"High CPU Usage: {cpu}%")
    if mem > MEM_THRESHOLD:
        alerts.append(f"High Memory Usage: {mem}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"Low Disk Space: {disk}%")

    if alerts:
        for alert in alerts:
            print(alert)
            logging.warning(alert)
    else:
        print("System is healthy")
        logging.info("System is healthy")

if __name__ == "__main__":
    check_system_health()