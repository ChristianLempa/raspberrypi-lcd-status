import psutil
from typing import Tuple


class MemoryMonitor:
    def __init__(self):
        pass

    def __call__(self) -> Tuple[str, str]:
        """Return memory utilization percentage and memory used/total."""
        memory_percent = self.get_memory_percentage()
        memory_usage = self.get_memory_usage()

        return memory_percent, memory_usage

    def get_memory_percentage(self) -> str:
        """Retrieve the current memory utilization percentage."""
        mem = psutil.virtual_memory()
        return f'Mem: {mem.percent}%'

    def get_memory_usage(self) -> str:
        """Retrieve the current memory usage in human-readable format."""
        mem = psutil.virtual_memory()
        # Convert bytes to MB for better readability on 16x2 LCD
        used_mb = mem.used / (1024 * 1024)
        total_mb = mem.total / (1024 * 1024)
        
        # For very large memory values, show in GB
        if total_mb > 1024:
            used_gb = used_mb / 1024
            total_gb = total_mb / 1024
            return f'{used_gb:.1f}GB/{total_gb:.1f}GB'
        else:
            return f'{used_mb:.0f}MB/{total_mb:.0f}MB'

