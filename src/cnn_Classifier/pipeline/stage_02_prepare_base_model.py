
from cnn_Classifier.config.configuration import ConfigurationManager
from cnn_Classifier.components.prepare_base_model import PrepareBAseModel
import logging
import unittest
import os

STAGE_NAME = "Prepare base model"

class MyTestCase(unittest.TestCase):
    def test_example(self):
        with self.assertRaisesRegex(ValueError,"invalid literal"):
            int("invalid")


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBAseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == '__main__':
    #unittest.main()


    # Define the output folder path
    output_dir = "artifacts/prepare_base_model"

    # Ensure the directory exists
    os.makedirs(output_dir, exist_ok=True)

    print(f"Output directory '{output_dir}' is ready.")

    try:
        logging.info(f"************************")
        logging.info(f">>>>>>>>>>stage{STAGE_NAME} started <<<<<<<<<<<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>stage{STAGE_NAME} completed <<<<<<<\n\nx==============x")
    except Exception as e:
        logging.exception(e)
        raise e