import os
import sys
import pandas as pd
import numpy as np
from src.employee.exception import CustomException
from src.employee.logger import logging
from src.employee.components.data_ingestion import DataIngestion
from src.employee.components.data_transformation import DataTransformation






class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_ingestion.inititate_data_ingestion()
        self.data_transformation = DataTransformation()
        self.data_transformation.inititate_data_transformation()
