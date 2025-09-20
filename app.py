from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataINgestion
from src.mlproject.components.data_ingestion import DataIngetsionConfig

import sys
if __name__ == "__main__":
    logging.info("The Execution has started")

    try:
        # data_ingestion_config = DataIngetsionConfig()
        data_ingestion = DataINgestion()
        data_ingestion.inititate_data_ingestion()

    except Exception as e:
        logging.info("custom Exception")
        raise CustomException(e, sys)
