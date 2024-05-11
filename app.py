from re import template
from flask import Flask, request, render_template,jsonify
from database import load_jobs_from_db
from sqlalchemy import text
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

print(__name__)
if (__name__ == "__main__" ) :
  print ("Inside if ")
  app.run(host="0.0.0.0",port=8080, debug=True)