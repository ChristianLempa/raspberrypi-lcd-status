import docker
from typing import Tuple, Optional


class ContainerMonitor:
  def __init__(self):
    """Initialize the Docker client."""

    try:
      self.client = docker.from_env()
    except Exception:
      self.client = None

  def __call__(self) -> Tuple[str, Optional[str]]:
    """Return the status of the Docker engine and container counts."""

    running_count, stopped_count, status = self.get_container_status()

    if status == "stopped":
      return f'Docker: {status}', None

    return f'Docker: {status}', f'{running_count} up / {stopped_count} down'

  def get_container_status(self) -> Tuple[int, int, str]:
    """Get the status of the Docker engine and count running and stopped containers."""

    if self.client is None:
      return 0, 0, "stopped"

    try:
      self.client.ping()
      docker_engine_status = "running"
    except Exception:
      return 0, 0, "stopped"

    containers = self.client.containers.list(all=True)
    running_count = sum(1 for container in containers if container.status == 'running')
    stopped_count = sum(1 for container in containers if container.status in ['exited', 'dead', 'created', 'paused'])

    return running_count, stopped_count, docker_engine_status
