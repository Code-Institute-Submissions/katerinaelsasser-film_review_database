# import section
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

#mongodb
app = Flask(__name__)
app.config['MONGO_URI'] = os.environ["MONGO_URI"]
app.config['MONGO_DBNAME'] = os.environ['MONGO_DBNAME']
mongo = PyMongo(app)

#Home Page
@app.route('/', methods=['GET', 'POST'])
@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template("pages/index.html") 

#viewfilms page
@app.route('/viewfilms', methods=['GET', 'POST'])
def viewfilms():
    return render_template("pages/viewfilms.html")

#viewreviews page
@app.route('/viewreviews', methods=['GET', 'POST'])
def viewfilms():
    return render_template("pages/viewreviews.html")

#addreviews page
@app.route('/addreviews', methods=['GET', 'POST'])
def viewfilms():
    return render_template("pages/addreviews.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)