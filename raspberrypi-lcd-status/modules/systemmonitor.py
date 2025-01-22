import psutil

class SystemMonitor:
  def __init__(self, show_mem=True):
    self.show_mem = show_mem

  def __call__(self):
    # Prepare the output strings
    cpu_output = self.get_cpu_load()
    mem_output = self.get_memory_utilization() if self.show_mem else None

    return cpu_output, mem_output

  def get_cpu_load(self):
    return f'CPU: {psutil.cpu_percent(interval=1)}%'

  def get_memory_utilization(self):
    mem = psutil.virtual_memory()
    return f'Mem: {mem.percent}%'
