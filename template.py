import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name=input("enter your project name:")
    if project_name !='':
        break

logging.info(f"created project by name: {project_name}")

list_of_files = [
    ".github/workflows/.gitkeep",
    "github/workflows/main.yaml",
    #f"src/(project_ame)/__init__.py",
    f"{project_name}/__init__.py",
    F"{project_name}/components/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/config.py",
    f"{project_name}/exception.py",
    f"{project_name}/predictor.py",
    f"{project_name}/utils.py",
    f"config/config.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "data_dump.py",
    "README.md"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating a new dir {filedir} and for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creatig a new file: {filename} for path: {filepath}")

    else:
        logging.info(f"file is already present at: {filepath}")