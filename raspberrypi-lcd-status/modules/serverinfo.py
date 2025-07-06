import socket
import psutil
from typing import Tuple, Optional


class ServerInfo:
  def __init__(self, show_ip: bool = False, iface: str = "eth0", **kwargs):
    """Initialize ServerInfo.
    
    Args:
        show_ip: Whether to display IP address
        iface: Network interface to get IP from
        **kwargs: Additional keyword arguments (ignored for backward compatibility)
    """
    self.server_name = self.get_server_name()[:16]
    self.show_ip = show_ip
    self.ip_address = self.get_ip_address(iface) if show_ip else None
    
    # Log any unrecognized parameters for debugging
    if kwargs:
      unrecognized_params = list(kwargs.keys())
      print(f"INFO: ServerInfo ignoring unrecognized parameters: {unrecognized_params}")

  def __call__(self) -> Tuple[str, Optional[str]]:
    """Return the server name and IP address if requested."""
    return self.server_name, self.ip_address if self.show_ip else None

  def get_server_name(self) -> str:
    """Retrieve the server name (hostname)."""
    return socket.gethostname()

  def get_ip_address(self, interface: str) -> str:
    """Retrieve the server's IP address for the specified interface."""
    try:
      addrs = psutil.net_if_addrs()
      if interface in addrs:
        for addr in addrs[interface]:
          if addr.family == socket.AF_INET:  # IPv4
            return addr.address
      return f"Interface '{interface}' not found or has no IPv4 address."
    except Exception as e:
      return f"Error retrieving IP address for interface '{interface}': {e}"
