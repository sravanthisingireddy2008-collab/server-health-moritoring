import psutil
import time
import logging
import os

# Create logs directory
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/server_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Set usage thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


def monitor_server():

    print("====================================")
    print(" SERVER HEALTH MONITORING SYSTEM")
    print("====================================")

    while True:

        # Monitor CPU
        cpu = psutil.cpu_percent(interval=1)

        # Monitor RAM
        memory = psutil.virtual_memory()
        ram = memory.percent

        # Monitor Disk
        disk = psutil.disk_usage("/")
        disk_usage = disk.percent

        print("\n------ SERVER HEALTH STATUS ------")

        print(f"CPU Usage    : {cpu}%")
        print(f"Memory Usage : {ram}%")
        print(f"Disk Usage   : {disk_usage}%")

        alert_found = False

        # CPU alert
        if cpu > CPU_THRESHOLD:
            print("ALERT: High CPU Usage!")
            logging.warning("High CPU usage: %.2f%%", cpu)
            alert_found = True

        # RAM alert
        if ram > MEMORY_THRESHOLD:
            print("ALERT: High Memory Usage!")
            logging.warning("High Memory usage: %.2f%%", ram)
            alert_found = True

        # Disk alert
        if disk_usage > DISK_THRESHOLD:
            print("ALERT: High Disk Usage!")
            logging.warning("High Disk usage: %.2f%%", disk_usage)
            alert_found = True

        if not alert_found:
            print("Server Status: HEALTHY")
            logging.info("Server is healthy")

        print("------------------------------------")

        time.sleep(5)


if __name__ == "__main__":

    try:
        monitor_server()

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        logging.info("Monitoring stopped by user.")