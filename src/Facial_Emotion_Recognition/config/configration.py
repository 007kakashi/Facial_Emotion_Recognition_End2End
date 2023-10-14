from src.Facial_Emotion_Recognition.constant import *
from src.Facial_Emotion_Recognition.utils.common import read_yaml,create_directories
from src.Facial_Emotion_Recognition.entity.config_entity import DataIngestionConfig,PrepareBaseModel_Arguments
from src.Facial_Emotion_Recognition.logger import logger

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
    
    def get_prepare_base_model_config(self) -> PrepareBaseModel_Arguments:
        
        config=self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config= PrepareBaseModel_Arguments(

            base_model_path=config.base_model_path,
            root_dir=config.root_dir,
            updated_base_model_path=config.updated_base_model_path,
            params_classes=self.params.CLASSES,
            params_image_size=self.params.IMAGE_SIZE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_learning_rate=self.params.LEARNING_RATE,
             
        )      

        logger.info('config of base model has prepared')

        return prepare_base_model_config    
                 
    
    