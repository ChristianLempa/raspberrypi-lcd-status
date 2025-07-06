## What's New

### Version 0.0.3 - Enhanced Backward Compatibility
- Enhanced backward compatibility with comprehensive error handling
- All monitor classes now gracefully handle unknown configuration parameters
- Improved warning messages and user guidance for migration
- Added comprehensive test suite for backward compatibility validation
- Enhanced documentation with detailed migration guide
- Better error handling in main application with LCD error display

### Version 0.0.2 - Module Separation
- **MemoryMonitor** is now a separate module from **SystemMonitor**
- **SystemMonitor** now only handles CPU monitoring (load average and utilization)
- **MemoryMonitor** handles memory usage and free memory display
- The old `show_mem` parameter in SystemMonitor is deprecated but supported for backward compatibility
- Updated configuration examples to reflect the new module structure

## Changelog

### [0.0.3] - 2025-07-06
- Enhanced backward compatibility with deprecated parameter handling
- Added comprehensive error handling for unknown configuration parameters
- Improved warning messages and user guidance for migration
- Added test suite for backward compatibility validation
- Enhanced documentation with migration guide
- All monitor classes now gracefully handle unknown parameters

### [0.0.2] - 2025-05-23
- Split SystemMonitor into separate CPU and Memory monitors
- Created new MemoryMonitor for memory statistics
- Updated configuration format to support separate monitors
- Improved display formatting for 16x2 LCD compatibility

### [0.0.1] - Initial Release
- Initial Release of the package
