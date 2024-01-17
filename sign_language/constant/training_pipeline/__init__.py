import os

ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://github.com/Naveen6220/extracting_demo_repo/raw/main/Sign_language_data.zip"




"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yaml"]


"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5m.pt"

MODEL_TRAINER_NO_EPOCHS: int = 2

MODEL_TRAINER_BATCH_SIZE: int = 32



"""
MODEL PUSHER related constant start with MODEL_PUSHER var name
"""
BUCKET_NAME = "sign-lang-24"
S3_MODEL_NAME = "best.pt"
