import os
import yaml
from typing import Dict, Any


# Load configuration from YAML file
def load_config(filename: str) -> Dict[str, Any]:
  """Load and return the monitoring configuration from a YAML file."""
  if not os.path.isfile(filename):
    raise FileNotFoundError(f"Configuration file '{filename}' not found.")

  if os.path.getsize(filename) == 0:
    raise ValueError(f"Configuration file '{filename}' is empty.")

  try:
    with open(filename, 'r') as file:
      config = yaml.safe_load(file)
      if 'monitoring' not in config:
        raise KeyError("The configuration file must contain a 'monitoring' section.")
      return config['monitoring']
  except yaml.YAMLError as e:
    raise ValueError(f"Error parsing YAML file '{filename}': {e}")
  except Exception as e:
    raise ValueError(f"An error occurred while loading the configuration: {e}")
