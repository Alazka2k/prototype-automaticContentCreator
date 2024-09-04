import os
import shutil
from datetime import datetime
import logging
from error_handler import FileOperationError
from error_codes import ErrorCode, get_error_message

def handle_old_output_files(file_paths, output_folder="content/output", old_output_folder="old_output"):
    # Create the old_output folder inside the output folder if it doesn't exist
    old_output_path = os.path.join(output_folder, old_output_folder)
    if not os.path.exists(old_output_path):
        os.makedirs(old_output_path)

    # Current timestamp for file renaming
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for file_path in file_paths:
        if os.path.exists(file_path):
            # Construct the new file name with timestamp
            new_file_name = f"{timestamp}_{os.path.basename(file_path)}"
            new_file_path = os.path.join(old_output_path, new_file_name)

            try:
                shutil.move(file_path, new_file_path)
            except PermissionError:
                error_message = get_error_message(ErrorCode.PERMISSION_ERROR)
                raise FileOperationError(ErrorCode.PERMISSION_ERROR, f"{error_message}: {file_path}")

def create_image_folders(csv_file_path, img_folder_name):
    output_folder = os.path.dirname(csv_file_path)
    img_folder = os.path.join(output_folder, img_folder_name)
    
    if os.path.exists(img_folder):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        old_img_folder = f"{img_folder}_{timestamp}"
        shutil.move(img_folder, old_img_folder)
    
    os.makedirs(img_folder)

# File paths of the output files
output_files = ["video_script.csv", "video_content.csv"]
