import psutil
import datetime
import os

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 80.0
LOG_FILE = "system_monitor.log"

def log_alert(metric_name, current_value):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_message = f"[{timestamp}] 🔥 ALERT: High {metric_name} utilization detected: {current_value}%\n"
    
    print(alert_message.strip())
    with open(LOG_FILE, "a") as f:
        f.write(alert_message)

def monitor_system():
    
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    if cpu_usage > CPU_THRESHOLD:
        log_alert("CPU", cpu_usage)
    if memory_usage > MEMORY_THRESHOLD:
        log_alert("Memory", memory_usage)
    if disk_usage > DISK_THRESHOLD:
        log_alert("Disk Space", disk_usage)

if __name__ == '__main__':
    monitor_system()
