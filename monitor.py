import psutil
from config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD 
from logger import logger
from process_monitor import check_process
 
print("===== Server Health Monitor =====")
 
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
from logger import logger
 
logger.info(f"CPU: {cpu}%")
logger.info(f"Memory: {memory}%")
logger.info(f"Disk: {disk}%")


print(f"CPU Usage    : {cpu}%")
print(f"Memory Usage : {memory}%")
print(f"Disk Usage   : {disk}%")
 
print("\n------ Health Status ------")
 
if cpu > CPU_THRESHOLD:
    print("⚠️ CPU usage is HIGH!")
else:
    print("✅ CPU usage is Normal")
 
if memory > MEMORY_THRESHOLD:
    print("⚠️ Memory usage is HIGH!")
else:
    print("✅ Memory usage is Normal")
 
if disk > DISK_THRESHOLD:
    print("⚠️ Disk usage is HIGH!")
else:
    print("✅ Disk usage is Normal")
 
print("\n===== Process Status =====")
 
processes = ["python", "Code", "powershell"]
 
for process in processes:
    if check_process(process):
        print(f"✅ {process} is running")
    else:
        print(f"❌ {process} is NOT running")