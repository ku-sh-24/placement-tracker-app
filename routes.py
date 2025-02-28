# print("this is my db file")

# db = 10

# if __name__ == "__main__":
#   # this will not get executed bc name != main when we run app.py
#   # but this will execute when i run db.py
  
#   print("This file is executed directly")

from app import app, db
from flask import request, jsonify
from models import Job

#get all jobs
# to be able to create a route we will create a decorator

@app.route("/api/jobs", methods=["GET"])

def get_jobs():
  jobs = Job.query.all()
  # So instead of using SQL query we are using python code to get the data
  result = [job.to_json() for job in jobs]
  # [{..},{..},{..}] this is getting stored in result

  return jsonify(result) #, 200

# Create a job

# @app.route("/api/jobs",methods=["POST"])
# def create_job():
#   try:
#     data = request.json