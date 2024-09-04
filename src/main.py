import openai
import json
import os
import datetime
import logging
from config_manager import load_credentials
from csv_manager import read_csv, write_to_csv
from api_manager import get_chatgpt_response
from data_parser import parse_response
from file_manager import handle_old_output_files
from dynamic_prompt_generator import generate_dynamic_prompt
from logging.handlers import RotatingFileHandler
from error_handler import FileOperationError, ConfigurationError, CustomError

# Create 'logs' directory if it doesn't exist
logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Generate a timestamp
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Set up logging to file
log_filename = os.path.join(logs_dir, f'log_{timestamp}.txt')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[RotatingFileHandler(log_filename, maxBytes=1000000, backupCount=5),
                              logging.StreamHandler()])

# Set up logging
logger = logging.getLogger('openai')
logger.setLevel(logging.INFO)

# File paths of the output files
output_files = [
    os.path.join('content', 'output', 'video_script.csv'),
    os.path.join('content', 'output', 'video_content.csv')
]

def main():
    logging.debug("Handling old output files...")
    handle_old_output_files(output_files, output_folder="content/output")
    logging.debug("Old output files have been handled.\n")

    logging.debug("Loading credentials...")
    credentials = load_credentials()
    openai.api_key = credentials['api_key']
    logging.debug("Credentials loaded.\n")

    # Load dynamic prompt configuration from JSON
    logging.debug("Loading parameters from JSON...")
    try:
        with open(os.path.join('content', 'input', 'parameters.json'), 'r') as config_file:
            config = json.load(config_file)
    except Exception as e:
        logging.error(f"Failed to load parameters: {e}")
        return  # Stop execution if parameters are not loaded

    # Generate dynamic prompt
    logging.debug("Generating dynamic prompt...")
    initial_prompt = generate_dynamic_prompt(
        os.path.join('content', 'input', config['promptFile']), config['parameters'])
    logging.debug("Dynamic prompt generated.\n")

    logging.debug("Reading names from input CSV...")
    input_file_path = os.path.join('content', 'input', config['inputFile'])
    names = read_csv(input_file_path)
    logging.debug("Names loaded...")

    # Define script_fields and content_fields outside the loop
    scene_amount = int(config['parameters']['sceneAmount'])
    script_fields = ["Title", "Description", "Hashtags", "Opening_Scene"] + \
                    [f"Scene_{i}" for i in range(1, scene_amount + 1)] + ["Closing_Scene"]
    content_fields = ["Name", "Title_Visual_Prompt", "Opening_Scene_Visual_Prompt"] + \
                     [f"Scene_{i}_Visual_Prompt" for i in range(1, scene_amount + 1)] + ["Closing_Scene_Visual_Prompt"]

    video_script_rows = []
    video_content_rows = []

    for name in names:
        response = get_chatgpt_response(initial_prompt, name, openai)
        logging.debug(f"Response from OpenAI for {name}: {response}")

        if response:
            logging.debug("Processing response...")
            
            script_row = [
                response.title,
                response.description,
                response.hashtags,
                response.opening_scene.description
            ] + [scene.description for scene in response.scenes] + [response.closing_scene.description]
            
            content_row = [
                name,
                response.title,
                response.opening_scene.visual_prompt
            ] + [scene.visual_prompt for scene in response.scenes] + [response.closing_scene.visual_prompt]

            video_script_rows.append(script_row)
            video_content_rows.append(content_row)

            logging.debug(f"Script Row for {name}: {script_row}")
            logging.debug(f"Content Row for {name}: {content_row}\n")
        else:
            logging.debug(f"No response for prompt: {name}, skipping...\n")

    logging.debug("Writing data to CSV files...")
    write_to_csv(os.path.join('content', 'output', 'video_script.csv'), script_fields, video_script_rows)
    write_to_csv(os.path.join('content', 'output', 'video_content.csv'), content_fields, video_content_rows)
    logging.debug("Data successfully written to CSV files.")

if __name__ == "__main__":
    try:
        main()
    except (FileOperationError, ConfigurationError, CustomError) as e:
        logging.error(f"An error occurred: {e}")
        # The error will be displayed in the console with the message from error_codes.json