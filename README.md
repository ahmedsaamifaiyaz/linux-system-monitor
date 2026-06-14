# Linux Server Monitoring & Automation Script

## Project Overview
This project establishes a lightweight, automated monitoring solution for Linux server environments. Instead of manually inspecting system resources, a custom Python script continuously tracks core performance metrics (CPU utilization, memory allocation, and disk space usage). 

The script is designed to be scheduled via the native Linux `cron` daemon to run at regular intervals, capturing anomalies and writing time-stamped alerts to a log file for rapid troubleshooting and root-cause analysis.

## Tech Stack
* **Operating System:** Linux
* **Language:** Python 3.x
* **Core Libraries:** `psutil` (Process and system utilities)
* **Automation Scheduler:** Linux Cron Daemon

## Step-by-Step Execution Guide

### Step 1: Install System Dependencies
Ensure you have Python and pip installed, then install the required `psutil` tracking library:
```bash
pip install -r requirements.txt
```
## Step 2: Test the Script Manually
Run the tracking script manually to verify it executes without errors:
```bash
python monitor.py
```
### Step 3: Automate via Linux Crontab
To make the script run automatically every single minute in the background on a Linux server, open your cron editor:
```bash
crontab -e
```
* * * * * /usr/bin/python3 /absolute/path/to/monitor.py
