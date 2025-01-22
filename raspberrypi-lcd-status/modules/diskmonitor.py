import psutil

class DiskMonitor:
  def __init__(self):
    pass

  def __call__(self):
    disk_usage_output = self.get_disk_usage()
    return disk_usage_output

  def get_disk_usage(self):
    # Get disk usage statistics
    disk_usage = psutil.disk_usage('/')
    
    # Calculate total and available disk space in human-readable format
    total_disk = self.human_readable_size(disk_usage.total)
    available_disk = self.human_readable_size(disk_usage.free)
    free_percent = int((disk_usage.free / disk_usage.total) * 100)

    # Format the output string
    return f'Disk: {total_disk}', f'Free: {free_percent}%'

  def human_readable_size(self, size, decimal_places=1):
      """Convert bytes to a human-readable format, ensuring the string is no longer than 8 characters."""
      for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
          if size < 1024:
              formatted_size = f"{size:.{decimal_places}f}{unit}"
              # Ensure the output is no longer than 8 characters
              if len(formatted_size) > 8:
                  # Truncate the number and append the unit
                  return f"{size:.{decimal_places}f}"[:6] + unit  # Keep up to 6 characters for the number
              return formatted_size
          size /= 1024
      
      # Handle sizes larger than TB
      formatted_size = f"{size:.{decimal_places}f} PB"
      if len(formatted_size) > 8:
          return f"{size:.{decimal_places}f}"[:6] + "PB"  # Keep up to 6 characters for the number
      return formatted_size
