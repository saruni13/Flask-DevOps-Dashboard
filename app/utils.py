import subprocess
import time
import os

def get_git_info():
    try:
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
        date = subprocess.check_output(["git", "log", "-1", "--format=%cd"]).decode().strip()
        return {"commit": commit, "last_commit": date}
    except:
        return {"commit": "N/A", "last_commit": "N/A"}

def get_logs(log_file="log.txt"):
    try:
        with open(log_file, "r") as f:
            return f.readlines()[-10:]
    except:
        return ["No logs available."]

def get_uptime():
    try:
        return time.time() - os.stat("/proc/1").st_ctime
    except:
        return 0
