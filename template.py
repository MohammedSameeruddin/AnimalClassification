import os
from pathlib import Path
import logging

#intializing logging
logging.basicConfig(format='[%(asctime)s] %(levelname)s::%(module)s::%(funcName)s() %(message)s', level=logging.DEBUG)

#create project

project_name="AnimalClassification"

list_of_files=[
    ".github/workflows/getkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirement.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    file_path=Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory successfully")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) ==0):
        with open(file_path, 'w') as f:
            pass
    else:
        logging.info(f"file already exists")


        
     
