import os
import sys
import pandas as pd
import numpy as np
from src.employee.exception import CustomException
from src.employee.logger import logging
from src.employee.entity.config_entity import DataTransformationConfig,DataIngestionConfig
from src.employee.constant import *
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        self.transformation_config = DataTransformationConfig()
    
    def inititate_data_transformation(self):
        logging.info("Datatransformation initiated")

        logging.info("Read the data set Using Pandas")

        df = pd.read_csv(self.ingestion_config.RAW_DATA_PATH)
        logging.info("Data has been read")

        logging.info("Data transformation started and replace the ? value")
        df["workclass"]= df["workclass"].replace('?',"Private")
        df["occupation"]= df["occupation"].replace('?',"Prof-specialty")
        df["native-country"]= df["native-country"].replace('?',"United-States")
        logging.info("Missing Value has been replaced")

        logging.info("Label Encoding the Categorical features")
        le = LabelEncoder()
        for feature in CATEGORICAL_FEATURES:
            df[feature] = le.fit_transform(df[feature])
            logging.info("label encoding is finished")

        logging.info("mapthe income with 0 and 1")
        
        df["income"] = df["income"].map({'<=50K':0, '>50K':1})

        logging.info("split the data ino train and test data")
        train_data,test_data = train_test_split(df,test_size=0.2,random_state=42)

        train_data.to_csv(self.transformation_config.TRAIN_DATA_PATH)
        test_data.to_csv(self.transformation_config.TEST_DATA_PATH)

        logging.info("Data Transformation Completed")

        return(
            self.transformation_config.TRAIN_DATA_PATH,
            self.transformation_config.TEST_DATA_PATH,

        )







