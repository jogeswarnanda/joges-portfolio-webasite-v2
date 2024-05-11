from flask import Flask, jsonify, render_template

from database import load_job_from_db, load_jobs_from_db

app = Flask(__name__)
@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html",jobs=jobs,company_name="Joges")
@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    #print("TYPEEE##2:", type(jobs))
    jobs = [tuple(row) for row in jobs]
    return jsonify(jobs)
@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  #print("JOB##2:", job)
  #return jsonify(job)
  if not job:
    return "Not Found", 404
  else:
    return render_template("jobpage.html",job=job)

print(__name__)
if (__name__ == "__main__" ) :
  print ("Inside if ")
  app.run(host="0.0.0.0",port=8080, debug=True)