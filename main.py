from cpu_ram import check_cpu_ram
from disk import check_disk_space
from internet import check_internet
from logger import log_issue

def run_diagnostics():
    print('runing diagnostic.....\n')
    cpu_ram_check= check_cpu_ram
    print(cpu_ram_check)
    log_issue(cpu_ram_check)

    disk_status = check_disk_space
    print(disk_status)
    log_issue(disk_status)

    internet_status= check_internet
    print(internet_status)
    log_issue(internet_status)
   
    
if __name__=='__main__':
    run_diagnostics

