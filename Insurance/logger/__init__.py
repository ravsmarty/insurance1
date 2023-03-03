import logging
import os
from datetime import datetime
import os

#log file name

LOG_DIR = "Insurance.log"
CORRECT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d__%H-%M-%S')}.log"

LOG_FILE_NAME = f"log_{CORRECT_TIME_STAMP}.log"


#log directory
#CURRENT_TIME_STAMP = os.path.join(os.getcwd(),"logs")

#create folder if not available
os.makedirs(LOG_DIR, exist_ok=True)

#log file path

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    )
