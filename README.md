# Server Health Monitoring & Alert System
 
## Project Overview
 
This project is a Python-based Server Health Monitoring Tool developed for DevOps Automation. It monitors system resources, logs server health, stores historical data in a SQLite database, generates CSV reports, and runs automatically using a scheduler.
 
---
 
## Features
 
- CPU Monitoring
- Memory Monitoring
- Disk Monitoring
- Process Monitoring
- Logging
- Configurable Thresholds
- Automatic Scheduler
- SQLite Database Storage
- CSV Report Generation
- Git & GitHub Integration
 
---
 
## Technologies Used
 
- Python
- SQLite
- Git
- GitHub
- VS Code
 
Python Libraries:
- psutil
- schedule
- sqlite3
- csv
- logging
 
---
 
## Project Structure
 
```
server-health-monitor/
│
├── monitor.py
├── process_monitor.py
├── config.py
├── logger.py
├── scheduler.py
├── database.py
├── report.py
├── email_alert.py
├── requirements.txt
├── README.md
├── .gitignore
├── monitor.log
├── health_monitor.db
└── health_report.csv
```
 
---
 
## How to Run
 
Install dependencies:
 
```
py -m pip install -r requirements.txt
```
 
Run the monitor:
 
```
py monitor.py
```
 
Run automatically:
 
```
py scheduler.py
```
 
Generate CSV report:
 
```
py report.py
```
 
---
 
## Output
 
The project:
 
- Monitors CPU, Memory and Disk usage.
- Checks important running processes.
- Logs system health.
- Stores monitoring history in SQLite.
- Generates CSV reports.
- Supports Git version control.
 
---
 
## Future Enhancements
 
- Docker Support
- Email Alerts

 