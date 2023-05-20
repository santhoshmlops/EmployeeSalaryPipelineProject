import os
import sys
from dataclasses import dataclass
from src.employee.constant import *

# Data ingestion config
@dataclass
class DataIngestionConfig:
    ARTIFACTS_DIR = os.path.join(ARTIFACTS_DIR)
    TRAIN_DATA_DIR = os.path.join(ARTIFACTS_DIR, TRAIN_DATA_PATH)
    TEST_DATA_PATH = os.path.join(ARTIFACTS_DIR,TEST_DATA_PATH) 
    RAW_DATA_PATH = os.path.join(ARTIFACTS_DIR, RAW_DATA_PATH)


    # train_data_path = os.path.join("artifacts", "train.csv")
    # test_data_path = os.path.join("artifacts", "test.csv")
    # raw_data_path = os.path.join("artifacts", "raw.csv")

    

