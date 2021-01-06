from flask import Flask, redirect, render_template
from flask_pymongo import  PyMongo
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from scrape_mars import scrape_all

app = Flask(__name__)

conn = 'mongodb://localhost:27017/mars_db'
mongo = PyMongo(app,conn)

@app.route('/')
def index():
    mars_data = mongo.db.mars.find_one()
    return(render_template('index.html', mars_data=mars_data))

@app.route('/scrape')
def scrape():
    data_document = scrape_all()
    # mars.insert_one(data_document)
    mongo.db.mars.update_one({}, {'$set': data_document}, upsert=True)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)