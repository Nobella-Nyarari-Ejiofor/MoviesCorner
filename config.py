class Config:
    '''
    General configuration parent class
    '''
    pass



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


API_KEY = '11319835f3f642b08ffc5ed98495e990'
BASE_URL = 'https://newsapi.org/v2/{}?q=Apple&from=2022-01-25&sortBy=popularity&apiKey=11319835f3f642b08ffc5ed98495e990'