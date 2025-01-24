import os
from typing import Optional


class TemperatureMonitor:
  def __init__(self):
    pass

  def __call__(self) -> Optional[float]:
    """Return the temperature if requested."""
    return self.get_temperature(), None

  def get_temperature(self) -> Optional[float]:
    """Retrieve the temperature from the specified thermal zone."""
    try:
      temp_file_path = "/sys/devices/virtual/thermal/thermal_zone0/temp"
      if os.path.exists(temp_file_path):
        with open(temp_file_path, 'r') as temp_file:
          temp_str = temp_file.read().strip()  # Read and strip whitespace/newline
          temp = float(temp_str) / 1000  # Convert from millidegrees Celsius to degrees
          return f"CPU Temp: {temp:.0f} °C"
      else:
        return None
    except Exception as e:
      print(f"Error retrieving temperature: {e}")
      return None
