import os
from dataclasses import dataclass
from torch import device
from Xray.constant.training_pipeline import *


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.S3_data_folder:str = S3_DATA_FOLDER
        self.bucket_name:str = BUCKET_NAME
        self.artifact_dir:str = os.path.join(ARTIFACT_DIR,TIMESTAMP)
        self.data_path = os.path.join(
            self.artifact_dir,"data_ingestion",self.S3_data_folder
        )
        self.train_data_path: str = os.path.join(self.data_path, "train")

        self.test_data_path: str = os.path.join(self.data_path, "test")


@dataclass
class DataTransformationConfig:
    def __init__(self):
         #color config
         self.color_jitter_transforms: dict = {
            "brightness": BRIGHTNESS,
            "contrast": CONTRAST,
            "saturation": SATURATION,
            "hue": HUE,
         }

         #AUggumentation config
         self.RESIZE: int = RESIZE
         self.CENTERCROP: int = CENTERCROP
         self.RANDOMROTATION: int = RANDOMROTATION
         self.normalize_transforms: dict = {
             "mean" : NORMALIZE_LIST_1,
             "std" : NORMALIZE_LIST_2
         }

        #DataLoader config
         self.data_loader_parms: dict = {
             "batch_size" : BATCH_SIZE,
             "shuffle" : SHUFFLE,
             "pin_memory" : PIN_MEMORY
         }

         self.artifact_dir: str = os.path.join(
             ARTIFACT_DIR,TIMESTAMP,"data_transformation"
         )

         self.train_tranform_file:str = os.path.join(
             self.artifact_dir,TRAIN_TRANSFORMS_FILE
         )
         self.test_tranform_file:str = os.path.join(
             self.artifact_dir,TEST_TRANSFORMS_FILE
         )




        