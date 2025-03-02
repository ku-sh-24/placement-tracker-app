# when we import somthing then it will first execute that file

from flask import Flask
# import express from "express"

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# flask needs this, a configuration

CORS(app)
# 

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///jobs.db"

# for performance reasons, even in production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app) # db instance

#
import routes

with app.app_context():
  db.create_all()


if __name__=="__main__": # we only want to run it when we run it directly
  app.run(debug=True,host='0.0.0.0', port=5000) # this will run multiple times
