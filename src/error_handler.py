import logging
import functools

class CustomError(Exception):
    """Base class for custom exceptions"""
    pass

class ConfigurationError(CustomError):
    """Raised when there's an issue with configuration files"""
    pass

class FileOperationError(Exception):
    """Raised when file operations fail"""
    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.error_code}: {self.message}"

def handle_errors(logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except FileNotFoundError as e:
                logger.error(f"File not found: {e}")
                raise FileOperationError(f"File not found: {e}")
            except PermissionError as e:
                logger.error(f"Permission denied: {e}. Please ensure all files are closed and you have necessary permissions.")
                raise FileOperationError(f"Permission denied: {e}")
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON in configuration file: {e}")
                raise ConfigurationError(f"Invalid JSON in configuration file: {e}")
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
                raise
        return wrapper
    return decorator

def retry_on_error(max_retries=3, retry_delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (PermissionError, FileOperationError) as e:
                    if attempt < max_retries - 1:
                        logging.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {retry_delay} seconds...")
                        time.sleep(retry_delay)
                    else:
                        logging.error(f"Operation failed after {max_retries} attempts: {e}")
                        raise
        return wrapper
    return decorator