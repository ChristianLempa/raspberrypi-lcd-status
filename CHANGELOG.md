## What's New

### Module Separation
- **MemoryMonitor** is now a separate module from **SystemMonitor**
- **SystemMonitor** now only handles CPU monitoring (load average and utilization)
- **MemoryMonitor** handles memory usage and free memory display
- The old `show_mem` parameter in SystemMonitor is deprecated but supported for backward compatibility
- Updated configuration examples to reflect the new module structure

## Changelog

- Initial Release of the package
