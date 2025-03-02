# print("this is my db file")

# db = 10

# if __name__ == "__main__":
#   # this will not get executed bc name != main when we run app.py
#   # but this will execute when i run db.py
  
#   print("This file is executed directly")

from app import app, db
from flask import request, jsonify
from models import Job
import requests

#get all jobs
# to be able to create a route we will create a decorator

@app.route("/api/jobs", methods=["GET"])

def get_jobs():
  jobs = Job.query.all()
  # So instead of using SQL query we are using python code to get the data
  result = [job.to_json() for job in jobs]
  # [{..},{..},{..}] this is getting stored in result

  return jsonify(result) #, 200

# GET THE LOGO OF THE COMPANY
def fetch_logo(company):
    # Build the URL with the company name
    url = f"https://api.brandfetch.io/v2/search/{company}?c=1idbeVcXuzEqopbnQs7"
    
    # Send the GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        
        # Loop through each item in the response and find the 'icon' field
        for item in data:
            if 'icon' in item:  # Check if the 'icon' key exists
                return item['icon']  # Return the URL of the icon (logo)
        
        return "Icon not found"
    else:
        return f"Error: {response.status_code}"  # Return error if request fails

# Create a job
@app.route("/api/jobs",methods=["POST"])
def create_job():
  try:
    data = request.json

    # adding validations, i.e. if the user does not enter say a particulat field

    required_fields = ["company", "role", "description", "applyLink", "duration"]

    for fields in required_fields:
       if fields not in data:
          return jsonify({"error": f"Missing field {fields}"}), 400

    company = data.get("company")
    role = data.get("role")
    description = data.get("description")
    stipend = data.get("stipend")
    applyLink = data.get("applyLink")
    duration = data.get("duration")
    jdFile = data.get("jdFile")
    

    # fetch logo based on company name 
    imgUrl = fetch_logo(company)

    # jobId = "jobId",
    new_job = Job(company= company, role=role, description=description, 
                  stipend=stipend, applyLink=applyLink, duration=duration,
                  imgUrl=imgUrl, jdFile=jdFile)
    
    db.session.add(new_job)
    # git add all
    db.session.commit()
    # git commit

    # new_job.to_json()
    return jsonify({"msg":"job created successfully"}), 201
    # change the result to 201 -> this means something is being created
    
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500
    # 500 status code means 

@app.route("/api/jobs/<int:id>", methods=["DELETE"])
def delete_job(id):

   try:
      job = Job.query.get(id)
      if job is None:
         return jsonify({"error": "job not found"}), 404
      
      db.session.delete(job)
      db.session.commit()
      return jsonify({"msg": "job deleted"}), 200
      pass
   except Exception as e:
      db.session.rollback()
      return jsonify({"error": str(e)}), 500
   
@app.route("/api/jobs/<int:id>", methods=["PATCH"])
def update_job(id):
   try:
      job = Job.query.get(id)
      if job is None:
         return jsonify({"error": "job not found"}), 404
      
      data = request.json
      
      job.company = data.get("company",job.company)
      job.role = data.get("role",job.role)
      job.description = data.get("description",job.description)
      job.stipend = data.get("stipend",job.stipend)
      job.applyLink = data.get("applyLink",job.applyLink)
      job.duration = data.get("duration",job.duration)
      job.jdFile = data.get("jdFile",job.jdFile)

      db.session.commit()
      return jsonify(job.to_json()),200
   except Exception as e:
      db.session.rollback()
      return jsonify({"error": str(e)}), 500