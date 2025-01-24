from kubernetes import client, config
from typing import Tuple, Optional


class KubernetesMonitor:
  def __init__(self):
    """Initialize the Kubernetes client."""
    try:
      config.load_kube_config("/etc/rancher/k3s/k3s.yaml")
      self.api = client.CoreV1Api()
    except Exception as e:
      print(f"Error initializing Kubernetes client: {e}")
      self.api = None

  def __call__(self) -> Tuple[str, Optional[str]]:
    """Return the status of the Kubernetes cluster and pod counts."""
    running_count, stopped_count, status = self.get_pod_status()
    namespaces_count = self.get_namespace_count()

    if status == "stopped":
      return f'Kube: {status}', None

    return f'Kube: {status}', f'{running_count} Pods / {namespaces_count} Ns'

  def get_pod_status(self) -> Tuple[int, int, str]:
    """Get the status of the Kubernetes cluster and count running and stopped pods."""
    if self.api is None:
      return 0, 0, "stopped"

    try:
      nodes = self.api.list_node()
      kubernetes_status = "running" if nodes.items else "stopped"
    except Exception:
      return 0, 0, "stopped"

    # Get all pods in all namespaces
    pods = self.api.list_pod_for_all_namespaces(watch=False)
    running_count = sum(1 for pod in pods.items if pod.status.phase == 'Running')
    stopped_count = sum(1 for pod in pods.items if pod.status.phase in ['Pending', 'Succeeded', 'Failed', 'Unknown'])

    return running_count, stopped_count, kubernetes_status

  def get_namespace_count(self) -> int:
    """Get the count of all namespaces in the Kubernetes cluster."""
    if self.api is None:
      return 0

    try:
      namespaces = self.api.list_namespace()
      return len(namespaces.items)  # Return the count of namespaces
    except Exception as e:
      print(f"Error retrieving namespaces: {e}")
      return 0
