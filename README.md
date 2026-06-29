System Health Monitoring Project
 
Overview
This is a Python-based system health monitoring project that tracks CPU, Memory, and Disk usage.  
It stores data in a SQLite database, generates logs, and creates CSV reports for analysis.
 
This project demonstrates basic DevOps monitoring concepts.
 
---
 
Features
- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Process monitoring
- Logging system (monitor.log)
- Configurable thresholds
- Automatic scheduler
- SQLite database storage (health_monitor.db)
- CSV report generation (health_report.csv)
- Modular Python design
 
---
 
Tech Stack
- Python 3
- psutil
- SQLite3
- CSV module
- Logging module
- Git & GitHub
 
---
 
Project Structure
 
monitor.py
database.py
report.py
view_db.py
health_monitor.db
health_report.csv
monitor.log
README.md
 
---
How to Run the Project
 
1. Install dependencies
pip install psutil
 
2. Create database
python database.py
3. Start system monitoring
python monitor.py
4. Generate CSV report
python report.py
 
 
 
Output Files
 
- monitor.log. //Logs system activity
- health_monitor.db  //Stores historical system data
- health_report.csv  //Exported report for analysis
 
 
 
Learning Outcome
 
This project helps to understand:
 
- System monitoring concepts
- Data logging and persistence
- Database integration with Python
- Automation using schedulers
- Report generation
- Git version control workflow
 
 
 
Future Improvements
 
- Email/Slack alerts for high CPU usage
- Docker containerization
 
 
 
Author
Vishnupriya P