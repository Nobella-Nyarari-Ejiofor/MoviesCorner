from flask import Flask
from .config import DevConfig



#Initialising flask application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_pyfile('config.py')


from app import views
