
import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Create directories and files if they do not exist
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Ensure the directory exists
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Check if the file exists and create it if necessary
    if not os.path.exists(filepath):  # If file doesn't exist, create it
        try:
            with open(filepath, "w") as f:
                pass  # Creating an empty file
            logging.info(f"Creating empty file: {filepath}")
        except PermissionError as e:
            logging.error(f"Permission denied while creating file {filepath}: {e}")
    elif os.path.getsize(filepath) == 0:  # If the file exists but is empty
        try:
            with open(filepath, "w") as f:
                pass  # Rewriting the empty file
            logging.info(f"File exists but is empty. Rewriting: {filepath}")
        except PermissionError as e:
            logging.error(f"Permission denied while rewriting empty file {filepath}: {e}")
    else:
        logging.info(f"{filename} already exists and is not empty.")
