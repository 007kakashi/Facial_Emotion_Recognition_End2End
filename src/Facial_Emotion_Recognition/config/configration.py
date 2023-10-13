from src.Facial_Emotion_Recognition.constant import *
from src.Facial_Emotion_Recognition.utils.common import read_yaml,create_directories
from src.Facial_Emotion_Recognition.entity.config_entity import DataIngestionConfig
# from src.Facial_Emotion_Recognition.constant import *

class ConfigurationManager:

    # This class is used to manage the configuration of the application.
    def __init__(self,
                 config_filepath= CONFIG_FILE_PATH,
                 params_filepath= PARAMS_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)

        create_directories([self.config.artifacts_root]) #to get values by calling key and then it will create directories

    def get_data_ingetsion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion  #calling config.yaml values by key 

        create_directories([config.root_dir]) # also this 

        data_ingestion_config=DataIngestionConfig(

            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir

        )

        return data_ingestion_config
    
    