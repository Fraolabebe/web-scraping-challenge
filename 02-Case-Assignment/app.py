from flask import Flask, redirect, render_tamplate
from flask_pymongo import  PyMongo
import pandas as pd
import pymongo
from splinter import Browser 
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


#instatiate Flask App
app = Flask(__name__)
client = PyMongo(app, uri='mongodb://localhost:27017/mars_db')


@app.route('/')
def index():
    return(render_tamplate)
        # some code here
@app.route('/scrape')
def scrape():
    

    # Connect to mars_app database
    db = client.mars_app

    # Connect to mars collection
    mars = db.mars

    # Gather document to insert
    data_document = scrape_mars.scrape_all()

    #mars.insert_one(data_document)


    mars.update_one({}, {'$set': data_document}, upsert=True
    


if __name__ == '__main__':
    app.run(debug=True)