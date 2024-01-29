import os
from pathlib import Path  #to handle paths 
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s:')
project = "TextSummarizer"

#ususal files for a project template
list_files =[
    ".github/workflow/.gitkeep", #hidde file
    f"src/{project}/__init__.py", #constructor file
    f"src/{project}/components/__main__.py", 
    f"src/{project}/utils/{project}.py",
    f"src/{project}/utils/common.py",
    f"src/{project}/logging/__init__.py",
    f"src/{project}/config/__init__.py",
    f"src/{project}/config/configuration.py",
    f"src/{project}/pipeline/__init__.py",
    f"src/{project}/entity/__init__.py",
    f"src/{project}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir and not os.path.exists(filedir):
        os.makedirs(filedir ,exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created file: {filepath}")

    else:
        logging.info(f"{filename} already exists")


