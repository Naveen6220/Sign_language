import sys
from sign_language.logger import logging
from sign_language.pipeline.train_pipeline import TrainPipeline
from sign_language.exception import SignException


if __name__ == "__main__":
    object = TrainPipeline()
    object.run_pipeline()
    print("Executed successfully")