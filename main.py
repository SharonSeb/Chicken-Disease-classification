import os
import sys

from src.cnn_Classifier import logger
from src.cnn_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnn_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
import logging

'''if int(sys.version[0]) == 3:
    assertRaisesRegex
else:
    assertRaisesRegexp'''

STAGE_NAME = "Data Ingestion Stage"

try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise(e)


STAGE_NAME = "Prepare Base Model"

try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise(e)