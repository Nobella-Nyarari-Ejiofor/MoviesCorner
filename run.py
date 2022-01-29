from flask import Flask
import requests
import os 

app = Flask(__name__)

@app.route('/')
def home():
  return 'Welcome to the Jungle'