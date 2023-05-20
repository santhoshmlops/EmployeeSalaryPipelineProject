import os
import sys
from dataclasses import dataclass
from src.employee.constant import *

# Data ingestion config
@dataclass
class DataIngestionConfig:
    ARTIFACTS_DIR:str = os.path.join(ARTIFACTS_DIR)    
    RAW_DATA_PATH:str = os.path.join(ARTIFACTS_DIR, RAW_DATA_PATH)

@dataclass
class DataTransformationConfig:
    TRAIN_DATA_PATH = os.path.join(ARTIFACTS_DIR, TRAIN_DATA_PATH)
    TEST_DATA_PATH = os.path.join(ARTIFACTS_DIR,TEST_DATA_PATH) 