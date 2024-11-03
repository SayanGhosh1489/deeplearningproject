from datetime import datetime
from typing import List

import torch

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

#data ingetion constants
ARTIFACT_DIR: str = "artifact"
BUCKET_NAME: str = "lungxray"
S3_DATA_FOLDER: str = "data"

#data transformation
CLASS_LABEL_1: str = "NORMAL"
CLASS_LABEL_2: str = "PNEUMONIA"