# RaspberryPi LCD Status

The RaspberryPi LCD Status Monitor is a simple app, that prints useful information about the RaspberryPi device on an 16x2 LCD display.

## Features

- **SystemMonitor:** Prints the CPU and RAM usage
- **DiskMonitor:** Prints the Disk Size and Usage
- **ServerInfo:** Prints the IP Address and Hostname
- **ContainerMonitor:** Prints the number of running and stopped Containers
- **TemperatureMonitor:** Prints the CPU temperature
- **KubernetesMonitor:** Prints the number of Pods and Namespaces

## Configuration

An example configuration file, can be found in `example.config.yaml`. The configuration file is used to configure the LCD display and the monitors.

## Installation

Deploy the container on your RaspberryPi using the Compose file in `example.compose.yaml`.

```yaml
---
services:
  raspberrypi-lcd-status:
    image: ghcr.io/christianlempa/raspberrypi-lcd-status:latest
    container_name: raspberrypi-lcd-status
    network_mode: host
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:rw
      - /etc/rancher/k3s/k3s.yaml:/etc/rancher/k3s/k3s.yaml:ro
      - /sys/devices/virtual/thermal/thermal_zone0/temp:/sys/devices/virtual/thermal/thermal_zone0/temp:ro
      - ./config/config.yaml:/etc/raspberrypi-lcd-status/config.yaml:ro
    devices:
      - /dev/i2c-1
    restart: unless-stopped
```

## Docker Integration

The container needs access to the Docker socket to get information about the running containers. Pass the Docker socket to the container using the following volume mount:

```yaml
volumes:
  - /var/run/docker.sock:/var/run/docker.sock:rw
```

## Kubernetes Integration

> This is currently only supported for k3s.

The container also needs access to the Kubernetes configuration file to get information about the running Pods and Namespaces.

```yaml
volumes:
  - /etc/rancher/k3s/k3s.yaml:/etc/rancher/k3s/k3s.yaml:ro
```
