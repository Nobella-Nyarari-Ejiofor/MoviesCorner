from . import main
from flask import render_template
from newsapi import NewsApiClient
import json
# from pandas import pd
# import datetime

  
@main.route('/')
def home():
  newsapi = NewsApiClient(api_key='0aa9f5a46444443fb64afbece6ada52b')
  topheadlines = newsapi.get_top_headlines( sources='bbc-news')
  topperheadlines = newsapi.get_everything(  sources='bbc-news',language='en')
 #this articles is a dictionary . 
  articles = topheadlines['articles']
  sourcesOrigin = newsapi.get_sources()
  namesource = sourcesOrigin['sources']
  
  names = []
  descriptions = []
  urls = []


 
  desc = []
  news = []
  img =[]
  url =[]
  date=[]

  for i in range (len(namesource)):
    mysource = namesource[i]
    names.append(mysource['name'])
    descriptions.append(mysource['description'])
    urls.append(mysource['url'])


  for i in range (len(articles)):
    myarticles = articles[i]

    news.append(myarticles['title'])
    desc.append(myarticles['description'])
    img.append(myarticles['urlToImage'])
    url.append(myarticles['url'])
    # myarticles['publishedAt'] = pd.to_datetime(myarticles['publishedAt'], format='%Y/%m/%d ')
    date.append(myarticles['publishedAt'])

  mylist = zip(news,desc,url,date,img)
  mysource =zip(names,descriptions,urls)

  return render_template('index.html', topheadlines =topheadlines,context = mylist ,source = mysource,news = topperheadlines , )