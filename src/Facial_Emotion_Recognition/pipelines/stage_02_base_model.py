from src.Facial_Emotion_Recognition.config.configration import ConfigurationManager
from src.Facial_Emotion_Recognition.components.base_model import PrepareBaseModel




class PrepareBaseModel:

    def __init__(self) -> None:
        pass

    def main(self):

        config=ConfigurationManager()
        model_prepare=config.get_prepare_base_model_config()
        model=PrepareBaseModel(config=model_prepare)
        model.get_base_model()
        model.updated_base_model()

