# Automatic Content Creator for Apocalypse Chronicles

This project is an Automatic Content Creator designed to generate video scripts and visual prompts for YouTube content, specifically focused on apocalyptic scenarios. It utilizes OpenAI's GPT model to create engaging and creative scripts based on user inputs and predefined parameters.

## Current Status

The application is currently in development. It includes the following components:

- **API Integration**: Utilizes OpenAI's GPT model for generating video scripts.
- **Dynamic Prompt Generation**: Customizes prompts based on user-defined parameters.
- **CSV Management**: Reads input data and writes output scripts to CSV files.
- **Environment Management**: Uses `.env` files to manage configuration and API keys.
- **Error Handling**: Custom error handling for improved user experience.
- **File Management**: Handles old output files and creates image folders.

## Project Structure

- **src/**: Contains the main source code files
  - `api_manager.py`: Handles interaction with the OpenAI API.
  - `config_manager.py`: Loads environment variables and initial requests.
  - `csv_manager.py`: Manages reading from and writing to CSV files.
  - `data_parser.py`: Parses the response from the API.
  - `dynamic_prompt_generator.py`: Generates customized prompts based on parameters.
  - `file_manager.py`: Manages output files, moving old outputs to a designated folder.
  - `main.py`: The main script that orchestrates the entire process.
  - `models.py`: Defines Pydantic models for structured data handling.
  - `error_handler.py`: Defines custom error classes.
  - `error_codes.py`: Defines error codes and messages.
- **tests/**: Contains unit tests for the application.
- **docs/**: Contains project documentation
  - `installation.md`: Installation instructions
  - `usage.md`: Usage guide
  - `configuration.md`: Configuration details
  - `error_handling.md`: Information on error codes and handling
  - `api_reference.md`: Detailed API documentation
- `README.md`: Overview of the documentation

## Setup and Installation

For detailed installation instructions, please refer to [docs/installation.md](docs/installation.md).

## Usage

For information on how to use the Apocalypse Chronicles content creator, please see [docs/usage.md](docs/usage.md).

## Configuration

Details on how to configure the project can be found in [docs/configuration.md](docs/configuration.md).

## Error Handling

For information on error codes and how to handle errors, refer to [docs/error_handling.md](docs/error_handling.md).

## API Reference

For a detailed API reference, please see [docs/api_reference.md](docs/api_reference.md).

## Testing

Run tests using `unittest`:

```bash
python -m unittest discover tests
```


## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License.