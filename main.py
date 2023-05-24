from config import *
from classes import *
from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_index():
    candidatesall = candidates(path).all_candidates()
    return candidatesall


@app.route("/profile/<int:uid>")
def page_profile(uid):
    candidates_uid = candidates(path).profile_candidates(uid)
    return candidates_uid


@app.route("/skills/<skill>")
def page_skills(skill):
    candidates_skills = candidates(path).skills_candidates(skill)
    return candidates_skills


app.run(host='0.0.0.0', port=8000)
