from app import app
from flask import render_template
from newsapi import NewsApiClient
import json
import pandas as pd

  
@app.route('/')
def home():
  newsapi = NewsApiClient(api_key='11319835f3f642b08ffc5ed98495e990')
  topheadlines = newsapi.get_top_headlines( sources='bbc-news')
 #this articles is a dictionary . 
  articles = topheadlines['articles']
  sourcesOrigin = newsapi.get_sources()
  namesource = sourcesOrigin['sources']
  
  # name = []
  # description = []
  # urls = []


 
  desc = []
  news = []
  img =[]
  url =[]
  date=[]
  # for i in range (len(namesource)):
  #   mysource = namesource[i]
  #    name.append = 

  for i in range (len(articles)):
    myarticles = articles[i]

    news.append(myarticles['title'])
    desc.append(myarticles['description'])
    img.append(myarticles['urlToImage'])
    url.append(myarticles['url'])
    # myarticles['publishedAt'] = myarticles.to_datetime(myarticles['publishedAt'], format='%Y/%d/%m %H:%M:%S')
    date.append(myarticles['publishedAt'])
   


  mylist = zip(news,desc,url,date,img)

  return render_template('index.html', topheadlines =topheadlines , context = mylist )