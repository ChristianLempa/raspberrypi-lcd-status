import psutil
from typing import Tuple, Optional


class SystemMonitor:
  def __init__(self, show_mem: bool = True):
    self.show_mem = show_mem

  def __call__(self) -> Tuple[str, Optional[str]]:
    """Return CPU load and memory utilization if requested."""
    cpu_output = self.get_cpu_load()
    mem_output = self.get_memory_utilization() if self.show_mem else None

    return cpu_output, mem_output

  def get_cpu_load(self) -> str:
    """Retrieve the current CPU load percentage."""
    return f'CPU: {psutil.cpu_percent(interval=1)}%'

  def get_memory_utilization(self) -> str:
    """Retrieve the current memory utilization percentage."""
    mem = psutil.virtual_memory()
    return f'Mem: {mem.percent}%'
