from distutils.debug import DEBUG
class Config:
    '''
    General configurat3eerrfrfrfion parent class
    '''
    NEWS_API_KEY='0aa9f5a46444443fb64afbece6ada52b'
    # NEWS_API_KEY = '11319835f3f642b08ffc5ed98495e990'
    NEWS_BASE_URL = 'https://newsapi.org/v2/{}?q=Apple&from=2022-01-25&sortBy=popularity&apiKey=11319835f3f642b08ffc5ed98495e990'
    TOP_HEADLINES_URL  = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SOURCE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    CATEGORIES_BASE_URL= 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    SEARCH_NEWS_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    



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

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}


