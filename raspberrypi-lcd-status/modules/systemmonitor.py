import psutil
from typing import Tuple
import warnings


class SystemMonitor:
  """Monitor system CPU load average and utilization for display on a 16x2 LCD."""
  
  def __init__(self, show_mem=None, **kwargs):
    """Initialize the SystemMonitor.
    
    Args:
        show_mem: DEPRECATED. This parameter is no longer used. 
                 Use the separate MemoryMonitor class instead.
        **kwargs: Additional keyword arguments (ignored for backward compatibility).
    """
    # Handle backward compatibility for the old show_mem parameter
    if show_mem is not None:
      if show_mem:
        # Only warn if show_mem was True (user was expecting memory display)
        warnings.warn(
          "The 'show_mem' parameter in SystemMonitor is deprecated. "
          "Please use the separate 'MemoryMonitor' class to display memory information. "
          "See the updated example.config.yaml for the new configuration format.",
          DeprecationWarning,
          stacklevel=2
        )
        print("WARNING: SystemMonitor 'show_mem' parameter is deprecated. "
              "Please use the separate 'MemoryMonitor' class instead.")
      else:
        # If show_mem was False, just note that the parameter is ignored
        print("INFO: SystemMonitor 'show_mem' parameter is deprecated but ignored (was set to False).")
    
    # Log any unrecognized parameters for debugging
    if kwargs:
      unrecognized_params = list(kwargs.keys())
      print(f"INFO: SystemMonitor ignoring unrecognized parameters: {unrecognized_params}")

  def __call__(self) -> Tuple[str, str]:
    """Return CPU load average and CPU utilization percentage.
    
    Returns:
        Tuple[str, str]: First line contains load average (e.g., "Load: 0.12 0.34 0.56"),
                        second line contains CPU utilization (e.g., "CPU: 8.2%").
    """
    load_output = self.get_cpu_load_average()
    cpu_output = self.get_cpu_utilization()

    return load_output, cpu_output

  def get_cpu_load_average(self) -> str:
    """Retrieve the current CPU load average formatted for 16x2 LCD.
    
    Returns:
        str: Load average formatted as "Load: X.XX X.XX X.XX"
    """
    load_avg = psutil.getloadavg()
    return f'Load: {load_avg[0]:.2f} {load_avg[1]:.2f} {load_avg[2]:.2f}'

  def get_cpu_utilization(self) -> str:
    """Retrieve the current CPU utilization percentage.
    
    Returns:
        str: CPU utilization formatted as "CPU: X.X%"
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    return f'CPU: {cpu_percent}%'
