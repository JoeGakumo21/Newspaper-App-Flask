# from instance.config import NEWS_API_KEY
import os

class Config:
    '''
    General configuration parent class
    '''
NEWS_API_KEY ='https://newsapi.org/v2/everything?q=apple&from=2021-09-08&to=2021-09-08&sortBy=popularity&apiKey=6e5882a38e5f40e9bad1a2742e5d9c9e'
NEWS_API_KEY_URL='NEWS_API'
SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True