from Flask import Response
from prometheus_client import generate_latest, Gauge

cpu_gauge = Gauge('cpu_usage', 'CPU Usage')
mem_gauge = Gauge('memory_usage', 'Memory Usage')

@dashboard_bp.route("/metrics")
def metrics():
    cpu_gauge.set(psutil.cpu_percent())
    mem_gauge.set(psutil.virtual_memory().percent)
    return Response(generate_latest(), mimetype='text/plain')
