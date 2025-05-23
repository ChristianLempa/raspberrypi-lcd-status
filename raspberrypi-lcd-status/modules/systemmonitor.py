import psutil
from typing import Tuple


class SystemMonitor:
  def __init__(self):
    pass

  def __call__(self) -> Tuple[str, str]:
    """Return CPU utilization and load average."""
    cpu_output = self.get_cpu_utilization()
    load_output = self.get_cpu_load_average()

    return cpu_output, load_output

  def get_cpu_utilization(self) -> str:
    """Retrieve the current CPU utilization percentage."""
    return f'CPU: {psutil.cpu_percent(interval=1)}%'

  def get_cpu_load_average(self) -> str:
    """Retrieve the current CPU load average (1 and 5 min)."""
    load1, load5, _ = psutil.getloadavg()
    return f'Load: {load1:.1f}/{load5:.1f}'
