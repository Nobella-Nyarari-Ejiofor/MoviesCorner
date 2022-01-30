from app import app
from flask import render_template



  
@app.route('/')
def home():
  title = "Newscorner"
  return render_template('index.html', title = title)