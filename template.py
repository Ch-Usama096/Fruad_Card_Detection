import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO)

peojectName = "Fraud_Card_Detection"

listOfFiles = [

    f"src/{peojectName}/__init__.py",
    f"src/{peojectName}/components/__init__.py",
    f"src/{peojectName}/components/data_ingestion.py",
    f"src/{peojectName}/components/data_transformation.py",
    f"src/{peojectName}/components/model_traning.py",
    f"src/{peojectName}/components/model_monitering.py",
    f"src/{peojectName}/pipelines/__init__.py",
    f"src/{peojectName}/pipelines/training_pipeline.py",
    f"src/{peojectName}/pipelines/prediction_pipeline.py",
    f"src/{peojectName}/exception.py",
    f"src/{peojectName}/logger.py",
    f"src/{peojectName}/utils.py",
    "app.py",
    "setup.py",
    "requirements.txt"
]


# Creating the Folder and check the folder already exits or not
for filepath in listOfFiles:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")

