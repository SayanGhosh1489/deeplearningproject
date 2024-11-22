import os, sys
from Xray.cloud_storage.s3_ops_pusher import S3OperationPusher
from Xray.entity.config_entity import ModelPusherConfig
from Xray.entity.artifact_entity import ModelTrainingArtifcat
from Xray.logger import logging
from Xray.exception import XRayException


class ModelPusher:
    def __init__(self,
                 model_pusher_config: ModelPusherConfig,
                 model_training_artifact: ModelTrainingArtifcat
                 ) -> None:
        self.model_pusher_config = model_pusher_config
        self.s3 = S3OperationPusher()
        self.model_training_artifact = model_training_artifact

    def initiate_model_pusher(self):
        logging.info("Entered initiate_model_pusher method of ModelPusher Class")

        try:

            self.s3.upload_file(
                bucket_name= self.model_pusher_config.bucket_name,
                from_filename = self.model_training_artifact.trained_model_path,
                to_filename = self.model_pusher_config.model_name,
                remove= False
            )

            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")

        except Exception as e:
            raise XRayException(e,sys)
