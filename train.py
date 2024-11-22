import sys
from Xray.pipeline.training_pipeline import TrainPipeline
from Xray.exception import XRayException

def start_training():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

    except Exception as e:
        XRayException(e,sys)


if __name__ == "__main__":
    start_training()