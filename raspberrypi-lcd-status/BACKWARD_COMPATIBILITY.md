# Backward Compatibility Guide

This document explains how the Raspberry Pi LCD Status Monitor handles backward compatibility with older configuration formats.

## Overview

As of version 0.0.2, the `SystemMonitor` was split into separate `SystemMonitor` and `MemoryMonitor` classes to provide better modularity and display options. The application maintains backward compatibility with the old configuration format to ensure existing installations continue to work.

## Old vs New Configuration Format

### Old Format (pre-v0.0.2)
```yaml
monitoring:
  delay: 5
  items:
    - SystemMonitor:
        show_mem: true    # This parameter is now deprecated
```

### New Format (v0.0.2+)
```yaml
monitoring:
  delay: 5
  items:
    - SystemMonitor: {}     # Shows CPU load average and utilization
    - MemoryMonitor: {}     # Shows memory usage and free memory
```

## Backward Compatibility Behavior

### SystemMonitor with `show_mem` Parameter

1. **`show_mem: true`**
   - **Behavior**: Shows deprecation warning, continues to display CPU information only
   - **Warning Message**: "WARNING: SystemMonitor 'show_mem' parameter is deprecated. Please use the separate 'MemoryMonitor' class instead."
   - **Action Required**: Add a separate `MemoryMonitor` entry to your configuration

2. **`show_mem: false`**
   - **Behavior**: Shows info message, displays CPU information only (same as new format)
   - **Info Message**: "INFO: SystemMonitor 'show_mem' parameter is deprecated but ignored (was set to False)."
   - **Action Required**: Remove the `show_mem` parameter when convenient

### Unknown Parameters

All monitor classes gracefully handle unknown or deprecated parameters:

```yaml
- SystemMonitor:
    unknown_parameter: "value"    # Will be ignored with info message
    old_setting: 123             # Will be ignored with info message
```

**Info Message**: "INFO: SystemMonitor ignoring unrecognized parameters: ['unknown_parameter', 'old_setting']"

## Migration Guide

### Step 1: Update Your Configuration

Replace this:
```yaml
- SystemMonitor:
    show_mem: true
```

With this:
```yaml
- SystemMonitor: {}
- MemoryMonitor: {}
```

### Step 2: Test the Configuration

You can test your configuration file without affecting the running system:

```bash
python3 -c "from configuration import load_config; config = load_config('your_config.yaml'); print('Config loaded successfully')"
```

### Step 3: Restart the Service

After updating your configuration, restart the LCD monitor service to apply changes.

## Error Handling

The application includes robust error handling for backward compatibility issues:

- **Configuration errors**: Will be logged and display error messages on LCD
- **Unknown parameters**: Will be ignored with informational messages
- **Module loading errors**: Will be caught and reported without crashing

## Supported Monitor Classes

All monitor classes support unknown parameter handling:

- `SystemMonitor` - CPU load and utilization
- `MemoryMonitor` - Memory usage and free memory
- `DiskMonitor` - Disk usage statistics  
- `TemperatureMonitor` - CPU temperature
- `ContainerMonitor` - Docker container status
- `KubernetesMonitor` - Kubernetes cluster status
- `ServerInfo` - Server hostname and IP information

## Testing Backward Compatibility

You can test backward compatibility using the provided test scripts:

```bash
# Test individual monitor classes
python3 test_backward_compatibility.py

# Test full application integration
python3 test_app_integration.py

# Test with old configuration format
python3 test_app_integration.py test_old_config.yaml
```

## Best Practices

1. **Update configurations gradually**: The old format will continue to work, so you can update at your own pace
2. **Monitor logs**: Check for deprecation warnings in your logs to identify configurations that need updating
3. **Test changes**: Always test configuration changes in a development environment first
4. **Keep backups**: Maintain backup copies of working configurations before making changes

## Future Considerations

- The `show_mem` parameter support will be maintained for several versions
- Unknown parameter handling will continue to be supported
- Future versions may add new parameters that older configurations will safely ignore

## Getting Help

If you encounter issues with backward compatibility:

1. Check the application logs for error messages
2. Verify your YAML syntax is correct
3. Test with the provided test scripts
4. Review this documentation for migration guidance

For additional support, refer to the main README or submit an issue to the project repository.
