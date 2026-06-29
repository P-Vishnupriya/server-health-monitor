import sqlite3
import csv
 
conn = sqlite3.connect("health_monitor.db")
cursor = conn.cursor()
 
cursor.execute("SELECT * FROM system_health")
rows = cursor.fetchall()
 
with open("health_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
 
    writer.writerow(["ID", "Timestamp", "CPU", "Memory", "Disk"])
 
    writer.writerows(rows)
 
conn.close()
 
print("✅ Report generated successfully!")