from app import app
import urllib.request,json
from models import news

News = news.News

newsapi =f' https://newsapi.org/v2/top-headlines?country=us&apiKey=11319835f3f642b08ffc5ed98495e990'
