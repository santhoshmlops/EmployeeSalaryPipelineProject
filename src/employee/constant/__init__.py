import os
import sys

# Data ingestion constants
ARTIFACTS_DIR:str = "artifacts"
ADULT_DATA_DIR:str = "notebook/dataset"
ADULT_DATA_PATH:str = "adult.csv"
TRAIN_DATA_PATH:str = "train.csv"
TEST_DATA_PATH:str = "test.csv"
RAW_DATA_PATH:str = "raw.csv"


# Data Transformation Constant:
CATEGORICAL_FEATURES = ['workclass', 'education', 'marital-status', 'occupation','relationship', 'race', 'gender', 'native-country']
DROP = ["education","fnlwgt","native-country"]