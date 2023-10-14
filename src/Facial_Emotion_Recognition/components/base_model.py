
from src.Facial_Emotion_Recognition.constant import *
from src.Facial_Emotion_Recognition.utils.common import read_yaml,create_directories
from src.Facial_Emotion_Recognition.logger import logger
from src.Facial_Emotion_Recognition.entity.config_entity import PrepareBaseModel_Arguments
import tensorflow as tf

class PrepareBaseModel:

    def __init__(self, config: PrepareBaseModel_Arguments):
        self.config=config

    @staticmethod
    def save_model( path: Path, model: tf.keras.Model):
        model.save(path)

    def get_base_model(self):

        self.model=tf.keras.applications.vgg16.VGG16(
            weights=self.config.params_weights,
            input_shape=self.config.params_image_size,
            include_top=self.config.params_include_top
        )

        self.save_model(path=self.config.base_model_path, model=self.model)

        logger.info('base model has been saved')

    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        
        if freeze_all :
            for layer in model.layers:
                model.trainable = False
        
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in=tf.keras.layers.Flatten()(model.output)
        prediction=tf.keras.layers.Dense(
            activation='softmax',
            units=classes
        )(flatten_in)

        full_model=tf.keras.models.Model(

            inputs=model.input,
            outputs=prediction
            
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss='categorical_crossentrophy',
            metrics=['accuracy']
        )

        full_model.summary()

        # logger.info()

        return full_model
    

    # @staticmethod
    def updated_base_model(self):

        self.full_model=self.prepare_full_model(

            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )


