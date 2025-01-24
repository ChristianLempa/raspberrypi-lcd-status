# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install necessary packages for building RPi.GPIO and other dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    python3-rpi.gpio \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Set the working directory in the container
WORKDIR /raspberrypi-lcd-status

# Copy the current directory contents into the container at /raspberrypi-lcd-status
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "lcd_monitor.py"]
