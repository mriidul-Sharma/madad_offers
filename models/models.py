from flask_pymongo import PyMongo
from app import app

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/Offer")
db = mongodb_client.db