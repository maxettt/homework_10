from flask import Flask

import utils

app = Flask(__name__)

candidates = utils.load_candidates()

@app.route("/")
def page_index():
    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    str_candidates += '</pre>'
    return str_candidates

@app.route("/candidate/<int:id>")
def profile(id):
    candidate = candidates[id]
    str_candidates = f"<img src={candidate['picture']}></img> <br>{candidate['name']} <br>{candidate['position']} <br>{candidate['skills']} <br><br>"
    return str_candidates

@app.route("/skills/<skill>")
def skills(skill):
    str_candidates = '<pre>'
    for candidate in candidates.values():
        skills_candidate = candidate['skills'].split(', ')
        skills_candidate = [s.lower() for s in skills_candidate]
        if skill in skills_candidate:
            str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    str_candidates += '</pre>'
    return str_candidates

app.run(debug=True)





