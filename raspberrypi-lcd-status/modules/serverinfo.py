import socket
import psutil

class ServerInfo:
  def __init__(self, show_ip=False, iface="eth0"):
    self.server_name = self.get_server_name()[:16]
    self.show_ip = show_ip
    self.ip_address = self.get_ip_address(iface) if show_ip else None

  def __call__(self):
    return f"{self.server_name}", f"{self.ip_address}" if self.show_ip else None

  def get_server_name(self):
    """Retrieve the server name (hostname)."""
    return socket.gethostname()

  def get_ip_address(self, interface):
    """Retrieve the server's IP address."""
    try:
      # Get all network interfaces and their addresses
      addrs = psutil.net_if_addrs()
      if interface in addrs:
        for addr in addrs[interface]:
          if addr.family == socket.AF_INET:  # IPv4
            return addr.address
      return f"Interface '{interface}' not found or has no IPv4 address."
    except Exception as e:
      return f"Error retrieving IP address for interface '{interface}': {e}"
