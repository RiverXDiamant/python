# Checking Health of PC Exercise


import shutil
import psutil


# Define a check_disk_usage function that will receive a distant check and return true if there's more than 20 percent free or false if it's less.

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20



# Define a function called check_cpu_usage. Check the usage for a whole second. We'll say the machine is healthy, it a cpu_usage is less than 75 percent.