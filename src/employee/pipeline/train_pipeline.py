import os
import sys
import pandas as pd
import numpy as np
from src.employee.exception import CustomException
from src.employee.logger import logging
from src.employee.components.data_ingestion import DataIngestion





class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_ingestion.inititate_data_ingestion()
