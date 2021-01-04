from flask import Flask, redirect, render_tamplate
from flask_pymongo import  PyMongo@

app = Flask(__name__)
mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_db')

@app.route('/')
def home('/'):
    


if __name__ == '__main__':
    app.run()