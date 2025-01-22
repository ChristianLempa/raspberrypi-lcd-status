import os
import yaml

# Load configuration from YAML file
def load_config(filename):
  # Check if the file exists
  if not os.path.isfile(filename):
    raise FileNotFoundError(f"Configuration file '{filename}' not found.")

  # Check if the file is not empty
  if os.path.getsize(filename) == 0:
    raise ValueError(f"Configuration file '{filename}' is empty.")

  # Load and validate the YAML content
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
