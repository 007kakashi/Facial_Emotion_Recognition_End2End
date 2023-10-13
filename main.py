from src.Facial_Emotion_Recognition.logger import logger
from src.Facial_Emotion_Recognition.pipelines.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME='Data Ingestion Stage'

if __name__=='__main__':

    try:

        logger.info(f'>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<< ')
        
        pipeline=DataIngestionPipeline()
        pipeline.main()

        logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<< ')
    
    except Exception as e:
        logger.exception(e)
        raise e
