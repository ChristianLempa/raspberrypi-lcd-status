import logging
import os


def configure_logger(name=None):
  """Configure the logging settings."""
  log_level = os.getenv('LOG_LEVEL', 'INFO').upper()  # Default to INFO if not set
  numeric_level = getattr(logging, log_level, logging.INFO)
  logging.basicConfig(level=numeric_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

  return logging.getLogger(name)
