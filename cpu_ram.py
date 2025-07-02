import psutil
def check_cpu_ram():
    cpu_usage= psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    ram_usage = ram.percent
    status = f'cpu usage:{cpu_usage}%\nRAM usage:{ram_usage}%\n'
    if cpu_usage > 85 or ram_usage > 85:
        status+= 'high system usage '
    else:
        status += 'system usage is normal' 
    return status       