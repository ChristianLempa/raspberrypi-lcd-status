import psutil
from typing import Tuple


class MemoryMonitor:
  """Monitor system memory usage for display on a 16x2 LCD."""
  
  def __init__(self, **kwargs):
    """Initialize the MemoryMonitor.
    
    Args:
        **kwargs: Additional keyword arguments (ignored for backward compatibility).
    """
    # Log any unrecognized parameters for debugging
    if kwargs:
      unrecognized_params = list(kwargs.keys())
      print(f"INFO: MemoryMonitor ignoring unrecognized parameters: {unrecognized_params}")

  def __call__(self) -> Tuple[str, str]:
    """Return memory utilization percentage and free memory amount.
    
    Returns:
        Tuple[str, str]: First line contains memory utilization (e.g., "Mem: 37%"),
                        second line contains free memory (e.g., "Free: 123MB").
    """
    mem_usage_output = self.get_memory_usage()
    free_memory_output = self.get_free_memory()

    return mem_usage_output, free_memory_output

  def get_memory_usage(self) -> str:
    """Retrieve the current memory utilization percentage.
    
    Returns:
        str: Memory utilization formatted as "Mem: X%"
    """
    memory = psutil.virtual_memory()
    mem_percent = int(memory.percent)
    return f'Mem: {mem_percent}%'

  def get_free_memory(self) -> str:
    """Retrieve the current free memory amount in human-readable format.
    
    Returns:
        str: Free memory formatted as "Free: XXXMB" or "Free: X.XGB"
    """
    memory = psutil.virtual_memory()
    free_memory = self.human_readable_size(memory.available)
    return f'Free: {free_memory}'

  def human_readable_size(self, size: int, decimal_places: int = 1) -> str:
    """Convert bytes to a human-readable format, ensuring the string is no longer than 8 characters.
    
    Args:
        size: Size in bytes
        decimal_places: Number of decimal places to display
        
    Returns:
        str: Human-readable size string
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
      if size < 1024:
        formatted_size = f"{size:.{decimal_places}f}{unit}"
        # Ensure the output is no longer than 8 characters
        if len(formatted_size) > 8:
          return f"{size:.{decimal_places}f}"[:6] + unit  # Keep up to 6 characters for the number
        return formatted_size
      size /= 1024

    # Handle sizes larger than TB
    formatted_size = f"{size:.{decimal_places}f}PB"
    if len(formatted_size) > 8:
      return f"{size:.{decimal_places}f}"[:6] + "PB"  # Keep up to 6 characters for the number
    return formatted_size
