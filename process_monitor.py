import psutil
 
def check_process(process_name):
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] and process_name.lower() in process.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False