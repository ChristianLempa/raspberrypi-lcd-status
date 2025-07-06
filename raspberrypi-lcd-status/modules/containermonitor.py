import docker
from typing import Tuple, Optional
from logmanager import configure_logger


logger = configure_logger(__name__)


class ContainerMonitor:
  def __init__(self, **kwargs):
    """Initialize the Docker client.
    
    Args:
        **kwargs: Additional keyword arguments (ignored for backward compatibility)
    """
    # Log any unrecognized parameters for debugging
    if kwargs:
      unrecognized_params = list(kwargs.keys())
      print(f"INFO: ContainerMonitor ignoring unrecognized parameters: {unrecognized_params}")

    try:
      self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')
      logger.info("Docker client initialized successfully.")
    except Exception as e:
      logger.error(f"Failed to initialize Docker client: {e}")
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
      logger.info("Docker daemon is running.")
    except Exception as e:
      logger.error(f"Error pinging Docker daemon: {e}")
      return 0, 0, "stopped"

    containers = self.client.containers.list(all=True)
    running_count = sum(1 for container in containers if container.status == 'running')
    stopped_count = sum(1 for container in containers if container.status in ['exited', 'dead', 'created', 'paused'])

    logger.info(f"Found {running_count} running and {stopped_count} stopped containers.")
    return running_count, stopped_count, docker_engine_status
