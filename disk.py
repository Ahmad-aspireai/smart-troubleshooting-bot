def check_disk_space():
    total,used,free= shutil.disk_usage('/')
    free_gb= free // (2**30)