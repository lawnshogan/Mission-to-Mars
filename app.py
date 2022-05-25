# Use Flask to render a template, redirecting to another url, and creating a URL.
from flask import Flask, render_template, redirect, url_for
# Use PyMongo to interact with our Mongo database.
from flask_pymongo import PyMongo
# To use the scraping code, we will convert from Jupyter notebook to Python.
import scraping

# Set up Flask
app = Flask(__name__)

# Tell Python how to connect to Mongo using PyMongo
# tells Python that our app will connect to Mongo using a URI, 
# a uniform resource identifier similar to a URL.
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set up Flask routes

# Define route for HTML page
@app.route("/")
def index():
# uses PyMongo to find the "mars" collection in our database
   mars = mongo.db.mars.find_one()
# tells Flask to return an HTML template using an index.html file
   return render_template("index.html", mars=mars)

# Set up scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()