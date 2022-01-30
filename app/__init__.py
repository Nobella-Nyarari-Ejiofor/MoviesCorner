from flask import Flask


#Initialising flask application
app = Flask(__name__)

from app import views
