import psutil
from typing import Tuple


class DiskMonitor:
  def __init__(self):
    pass

  def __call__(self) -> Tuple[str, str]:
    """Return disk usage statistics."""
    disk_usage_output = self.get_disk_usage()
    return disk_usage_output

  def get_disk_usage(self) -> Tuple[str, str]:
    """Get disk usage statistics and format them."""
    # Get disk usage statistics
    disk_usage = psutil.disk_usage('/')

    # Calculate total and available disk space in human-readable format
    total_disk = self.human_readable_size(disk_usage.total)
    free_percent = int((disk_usage.free / disk_usage.total) * 100)

    # Format the output string
    return f'Disk: {total_disk}', f'Free: {free_percent}%'

  def human_readable_size(self, size: int, decimal_places: int = 1) -> str:
    """Convert bytes to a human-readable format, ensuring the string is no longer than 8 characters."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
      if size < 1024:
        formatted_size = f"{size:.{decimal_places}f}{unit}"
        # Ensure the output is no longer than 8 characters
        if len(formatted_size) > 8:
          return f"{size:.{decimal_places}f}"[:6] + unit  # Keep up to 6 characters for the number
        return formatted_size
      size /= 1024

    # Handle sizes larger than TB
    formatted_size = f"{size:.{decimal_places}f} PB"
    if len(formatted_size) > 8:
      return f"{size:.{decimal_places}f}"[:6] + "PB"  # Keep up to 6 characters for the number
    return formatted_size
