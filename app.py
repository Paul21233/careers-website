from re import L
from flask import Flask, jsonify, render_template

app = Flask(__name__)

jobs = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'San Fransisco',
    'salary': '$30000'
  },
  {
    'id': 2,
    'title': 'Soft. Dev',
    'location': 'LA',
    'salary': '$15000'
  },
  {
    'id': 3,
    'title': 'Fornt-end dev',
    'location': 'Arizona',
    'salary': '$20000'
  },
  {
    'id': 4,
    'title': 'Back-end Dev',
    'location': 'W. DC',
    'salary': '$25000'
  },
  {
    'id': 5,
    'title': 'Potato Dev',
    'location': 'NY',
    'salary': '$150000'
  }
]

@app.route('/')
def home_page():
  return render_template('home.html', jobs = jobs, CompanyName='Sowrin')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
