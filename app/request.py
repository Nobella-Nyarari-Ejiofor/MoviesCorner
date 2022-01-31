from flask import request
from app import app
import urllib.request,json
from .config import API_KEY, BASE_URL
from models import news

News = news.News

# api_key = app.config[API_KEY]
# base_url = app.config[BASE_URL]

# def getTheNews(category):
#   getTheNews_url = base_url.format(category,api_key)
  
