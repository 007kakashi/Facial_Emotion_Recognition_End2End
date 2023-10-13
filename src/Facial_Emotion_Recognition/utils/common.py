import os 
from box.exceptions import BoxValueError
import yaml
from src.Facial_Emotion_Recognition.logger import logger
import json
import joblib
# from ensure import ensure_annotaions
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


# @ensure_annotaions
def read_yaml(path_to_yaml: Path) ->ConfigBox:

    try:
        
        with open(path_to_yaml) as yaml_file:
            content= yaml.safe_load(yaml_file)
            logger.info(f'yaml file : {path_to_yaml} loaded successfully')
            return ConfigBox(content)

    except  BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    

# @ensure_annotaions
def create_directories(path_to_directories: list, verbos=True):
    
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbos:
            logger.info(f'created directories at :{path}')


# @ensure_annotaions
def save_json(path:Path, data:dict) ->ConfigBox:

    with open(path ,'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f'jason file has been saved at : {path}')


# @ensure_annotaions
def load_json(path:Path):

    with open(path) as f:
        json_file= json.load(f)

    logger.info(f'json file has been added from : {path}')
    return ConfigBox(json_file)

    
# @ensure_annotaions
def save_bin(data:Any, path:Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f'binary file has been created at : {path}')


# @ensure_annotaions
def load_bin(path:Path) -> Any:

    data= joblib.load(path)
    logger.info(f'binary file has been loaded from : {path}')

    return data


# @ensure_annotaions
def get_size(path:Path) -> str:

    size_in_kb=round(os.path.getsize(path)/1024)
    return f'{size_in_kb} KB'


def decode_image(imgstring ,filename):

    imgdata= base64.b64decode(imgstring)

    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encode_image_into_base64(cropped_image_path):

    with open(cropped_image_path, 'rb') as f:
        return base64.b64encode(f.read())





