from app import db


"""
  IF I CHANGE THE SCHEMA OF MY DB -> DELETE jobs.db AND RECREATE IT!!!!!
"""


class Job(db.Model):
  # job_id, company, role, desc, duration, stipend, image, jd_file
  jobId = db.Column(db.Integer, primary_key = True)
  company = db.Column(db.String(200), nullable = False)
  role = db.Column(db.String(100), nullable = False)
  description = db.Column(db.Text, nullable = False)
  stipend = db.Column(db.Text, nullable = False)
  applyLink = db.Column(db.String(200), nullable=False)
  duration = db.Column(db.Text, nullable = False)
  jdFile = db.Column(db.String(200), nullable=False)
  imgUrl = db.Column(db.String(200), nullable=False)

  def to_json(self):
    # when we send data to client we want to send it in the form of a json file,
    # so we create a function that will be called each time
    # self is the particular job that we are calling the method with

    return {
      "jobId":self.jobId,
      "company":self.company,
      "role":self.role,
      "description": self.description,
      "stipend": self.stipend,
      "applyLink": self.applyLink,
      "jdFile": self.jdFile,
      "duration": self.duration,
      "imgUrl": self.imgUrl,
    }