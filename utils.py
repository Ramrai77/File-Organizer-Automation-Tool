import os
import shutil
from config import SOURCE_FOLDER, FILE_TYPES

def organize_files():
    # Loop through all files in the folder
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file)[1].lower()
        moved = False

        # Check file category
        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                target_folder = os.path.join(SOURCE_FOLDER, folder_name)

                # Create folder if not exists
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, target_folder)
                moved = True
                break

        # Move unknown files to Others
        if not moved:
            other_folder = os.path.join(SOURCE_FOLDER, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, other_folder)
