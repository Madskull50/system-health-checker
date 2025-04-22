import psutil
import socket
import shutil
import platform

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    return f"CPU Usage: {usage}%"

def check_memory():
    memory = psutil.virtual_memory()
    return f"Memory Usage: {memory.percent}%"

def check_disk():
    total, used, free = shutil.disk_usage("/")
    return f"Disk Usage: {used // (2**30)} GB used of {total // (2**30)} GB"

def check_internet():
    try:
        socket.gethostbyname("google.com")
        return "Internet: Connected"
    except socket.error:
        return "Internet: Not Connected"

def get_system_info():
    return f"System: {platform.system()} {platform.release()}"

def main():
    print("System Health Report\n---------------------")
    print(get_system_info())
    print(check_cpu())
    print(check_memory())
    print(check_disk())
    print(check_internet())

if __name__ == "__main__":
    main()
