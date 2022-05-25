# Use Flask to render a template, redirecting to another url, and creating a URL.
from flask import Flask, render_template, redirect, url_for
# Use PyMongo to interact with our Mongo database.
from flask_pymongo import PyMongo
# To use the scraping code, we will convert from Jupyter notebook to Python.
import scraping

# Set up Flask
app = Flask(__name__)

# Tell Python how to connect to Mongo using PyMongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

