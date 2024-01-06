from mlProject.logging import logger
from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.components.data_transformation import DataTransformation
from pathlib import Path


STAGE_NAME = "Data Transformation stage"

class DataTransformaionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)