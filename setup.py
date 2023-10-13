import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description=f.read()

__version__='0.0.0'

REPO_NAME='Facial_Emotion_Recognition_End2End'
AUTHER_USER_NAME='007kakashi'
SRC_REPO='Facial_Emotion_Recognition'
AUTHER_EMAIL='upendrasgosavi@gmail.com'

setuptools.setup(

    name=SRC_REPO,
    version=__version__,
    auther=AUTHER_USER_NAME,
    auther_email=AUTHER_EMAIL,
    description='A small package for cnn app',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}',
    project_url={
        'bug tracker':f'https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'':'src'},
    pakages=setuptools.find_packages(where='src')

)