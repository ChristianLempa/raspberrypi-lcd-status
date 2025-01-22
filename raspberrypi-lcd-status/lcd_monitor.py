import time
import signal
import sys
import netifaces
import psutil
from RPLCD.i2c import CharLCD
from configuration import load_config


# Initialize the LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

# Flag to control the main loop
running = True

# Cleanup function to run on shutdown
def cleanup(signum, frame):
    global running
    running = False
    lcd.clear()  # Clear the LCD before shutting down
    lcd.write_string("Shutting down...")  # Display a message
    time.sleep(2)  # Wait a moment to show the message
    lcd.clear()  # Clear the LCD before exit program
    sys.exit(0)  # Exit the program gracefully

# Set up signal handlers
signal.signal(signal.SIGINT, cleanup)  # Handle Ctrl+C
signal.signal(signal.SIGTERM, cleanup)  # Handle termination signal

# Main function to update the LCD
def update_lcd(config):
  items = config['items']
  delay = config['delay']

  while running:
    for item in items:
      if not running:
        break
      lcd.clear()
      try:
        # Get the monitor class name and its options
        monitor_name, options = next(iter(item.items()))  # Extract the first item
        module_name = f'modules.{monitor_name.lower()}'
        module = __import__(module_name, fromlist=[''])

        # Ensure options is a dictionary, defaulting to an empty dict if None
        options = options if options is not None else {}

        # Instantiate the monitor class with the options
        monitor_class = getattr(module, monitor_name)
        monitor_instance = monitor_class(**options)  # Unpack options as keyword arguments

        # Call the instance to get the result
        first_line, second_line = monitor_instance()  # Now it returns two values

        if first_line:
            lcd.write_string(first_line)  # Write to the first line
        if second_line:
            lcd.cursor_pos = (1, 0)  # Move to the second line
            lcd.write_string(second_line)  # Write to the second line

      except ImportError:
        print(f'Module {item} not found')
      except Exception as e:
        print(f'Error: {str(e)}')

      # Wait for the specified delay before refreshing
      time.sleep(delay)


if __name__ == "__main__":
  try:
    config = load_config('/etc/raspberrypi-lcd-status/config.yaml')
    update_lcd(config)
  except (FileNotFoundError, ValueError, KeyError) as e:
    print(f"Configuration error: {e}")
