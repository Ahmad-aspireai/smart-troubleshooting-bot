
    
from datetime import datetime

def log_issue(status):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {status}\n"
    with open('system_log.txt', 'a') as log_file:
        log_file.write(log_entry)