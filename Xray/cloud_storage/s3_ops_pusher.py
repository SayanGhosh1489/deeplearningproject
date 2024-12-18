import os, sys
from io import StringIO
from typing import List, Union
import boto3
from botocore.exceptions import ClientError
from mypy_boto3_s3.service_resource import Bucket
from Xray.logger import logging
from Xray.exception import XRayException

class S3OperationPusher:
    def __init__(self) -> None:
        self.s3_client = boto3.client("s3")
        self.s3_resource = boto3.resource("s3")

    def upload_file(
            self,
            from_filename : str,
            to_filename: str,
            bucket_name: str,
            remove: bool = True
            ) ->None:
        logging.info("Entered the upload_file method of S3OperationPusher class")

        try:
            logging.info(f"{from_filename} file to {to_filename} file in {bucket_name} bucket")

            self.s3_client.upload_file(
                from_filename,bucket_name,to_filename
            )

            if remove is True:
                os.remove(from_filename)
                logging.info(f"Remove is set to {remove}, deleted the file")
            else:
                logging.info(f"Remove is set to {remove}, not deleted the file")
            logging.info("Exited the upload_file method of S3Operations class")

            logging.info(
                f"Uploaded {from_filename} file to {to_filename} file in {bucket_name} bucket"
            )
            
        except Exception as e:
            XRayException(e,sys)

    def download_file(
            self,
            bucket_name: str,
            model_path:str,
            model_name: str
    ):
        pass
            

