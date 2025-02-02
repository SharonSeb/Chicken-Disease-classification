import os
import sys

from src.cnn_Classifier import logger
from src.cnn_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnn_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnn_Classifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.cnn_Classifier.pipeline.stage_04_evaluation import EvaluationPipeline
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


STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e