import os
import sys
import pandas as pd
import numpy as np
from src.employee.exception import CustomException
from src.employee.logger import logging
from src.employee.entity.config_entity import DataIngestionConfig
from src.employee.constant import *



class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def inititate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            logging.info("Data Reading using Pandas library from local system")
            data = pd.read_csv(os.path.join(ADULT_DATA_DIR, ADULT_DATA_PATH))
            logging.info("Data Reading completed")

            os.makedirs((self.ingestion_config.ARTIFACTS_DIR), exist_ok=True)
            data.to_csv(self.ingestion_config.RAW_DATA_PATH, index=False)
            
            logging.info("Data Ingestion completed")

            return (
                self.ingestion_config.RAW_DATA_PATH,
               

            )
        except Exception as e:
            logging.info("Erro occured in data ingestion stage")
            raise CustomException(e, sys)