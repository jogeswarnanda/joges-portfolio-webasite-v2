from flask import Flask, jsonify, render_template,request,redirect,url_for,flash
from database import load_job_from_db, load_jobs_from_db,add_application_to_db

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

@app.route("/job/<id>/apply",methods=['GET', 'POST'])
def apply_to_job(id):
  job = load_job_from_db(id)
  
  if request.method == 'GET':
    data2 = []
    data2 = request.args
    print("GET DATDA:", data2)
    if not data2:
      return "Not Found", 404
    else:
      return render_template("txn.html",data2=data2)
  
  if request.method == 'POST':
      data = []
      data = request.form
        #data.append(
        #  request.form.get("full_name"),
        #)
        #data.append(
        #  request.form.get("email"),
        #)
      intValue = ord(id) - ord('0')
      id = int(id)
      print("intval:", intValue)
      print("POST DATA:", data)
      if not data:
        return "Not Found", 404
      else:
        add_application_to_db(id,data)
        return render_template("application_submitted.html",data=data,job=job)
        
      
print(__name__)
if (__name__ == "__main__" ) :
  print ("Inside if ")
  app.run(host="0.0.0.0",port=8080, debug=True)