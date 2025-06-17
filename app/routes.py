from flask import Blueprint, render_template
import psutil
from .utils import get_git_info, get_logs, get_uptime

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():
    sys_info = {
        "cpu": psutil.cpu_percent(),
        "mem": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
    }
    git_info = get_git_info()
    logs = get_logs()
    uptime = get_uptime()
    return render_template("dashboard.html", sys_info=sys_info, git_info=git_info, logs=logs, uptime=uptime)
