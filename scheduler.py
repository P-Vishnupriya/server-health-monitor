import schedule
import time
import subprocess
 
def run_monitor():
    print("Running Server Health Monitor...")
    subprocess.run(["py", "monitor.py"])
 
# Run every 60 seconds
schedule.every(60).seconds.do(run_monitor)
 
# Run once immediately when the scheduler starts
run_monitor()
 
print("Scheduler started. Monitoring every 60 seconds...")
 
while True:
    schedule.run_pending()
    time.sleep(1)