from src.Facial_Emotion_Recognition.entity.config_entity import DataIngestionConfig
from src.Facial_Emotion_Recognition.config.configration import ConfigurationManager
from src.Facial_Emotion_Recognition.components.data_ingestion import DataIngestion
from src.Facial_Emotion_Recognition.logger import logger



class DataIngestionPipeline():
    def __init__(self) -> None:
        pass


    def main(self):
    
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingetsion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()





