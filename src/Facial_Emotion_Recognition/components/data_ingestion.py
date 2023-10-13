import os
import urllib.request as request
from pathlib import Path
import zipfile
from src.Facial_Emotion_Recognition.logger import logger
from src.Facial_Emotion_Recognition.utils.common import get_size
from src.Facial_Emotion_Recognition.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config= config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename ,header =request.urlretrieve(

                url=self.config.source_url,
                filename= self.config.local_data_file
            )
            logger.info(f'{filename} downloaded with following info: {header}')

        else:
            logger.info(f'file already exists of size :{get_size(Path(self.config.local_data_file))}')


    def extract_zip_file(self):

        unzip_path= self.config.unzip_dir

        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_file:
            zip_file.extractall(unzip_path)
        
