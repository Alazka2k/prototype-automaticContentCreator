# API Reference

This document provides detailed information on the key modules, classes, and functions in the Apocalypse Chronicles project.

## `file_manager` Module

This module handles file operations, including moving and managing output files.

### `handle_old_output_files(file_paths, output_folder="content/output", old_output_folder="old_output")`

Moves old output files to a backup folder.

Parameters:
- `file_paths` (list of str): List of file paths to process.
- `output_folder` (str, optional): Main output folder. Defaults to "content/output".
- `old_output_folder` (str, optional): Subfolder for old files. Defaults to "old_output".

Raises:
- `FileOperationError`: If there's an issue moving files, particularly due to permission errors.

Example usage:

```python
from file_manager import handle_old_output_files
files_to_move = ["content/output/video_script.csv", "content/output/video_content.csv"]
handle_old_output_files(files_to_move)
```

## `error_handler` Module

This module defines custom error classes for the project.

### `class FileOperationError(Exception)`

Custom exception for file operation errors.

Attributes:
- `error_code` (int): Numeric code representing the error type.
- `message` (str): Descriptive error message.

Methods:
- `__init__(self, error_code, message)`: Initializes the exception with an error code and message.
- `__str__(self)`: Returns a string representation of the error.

Example usage:
```python
from error_handler import FileOperationError
from error_codes import ErrorCode
try:
# Some file operation
raise FileOperationError(ErrorCode.PERMISSION_ERROR, "Cannot access file")
except FileOperationError as e:
print(f"An error occurred: {e}")
```

## `error_codes` Module

This module defines error codes and provides utility functions for error handling.

### `class ErrorCode`

An enumeration of error codes used in the project.

Attributes:
- `FILE_NOT_FOUND` (int): Error code for file not found (value: 1001)
- `PERMISSION_ERROR` (int): Error code for permission denied (value: 1006)
- (Other error codes as defined in the project)

### `get_error_message(code)`

Retrieves the error message associated with a given error code.

Parameters:
- `code` (int): The error code.

Returns:
- str: The corresponding error message.

Example usage:

```python
from error_codes import ErrorCode, get_error_message
error_message = get_error_message(ErrorCode.PERMISSION_ERROR)
print(error_message) # Output: "Permission denied: The file is being used by another process"
```


## `main` Module

The main entry point for project.

### `main()`

The main function that orchestrates the content generation process.

This function:
1. Handles old output files
2. Generates new apocalyptic scenarios
3. Creates video scripts based on the scenarios
4. Manages output files and error handling

Example usage:

```python
from main import main
if name == "main":
main()
```

Note: The exact implementation details of `main()` may vary based on the current state of the project.

For more detailed information on each module and function, please refer to the inline documentation in the source code.

