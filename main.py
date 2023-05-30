from flask import Flask

from utils import get_all, load_candidates, get_by_pk, get_by_skill

FILENAME = 'candidates.json'
data = get_all(load_candidates(FILENAME))


app = Flask(__name__)


@app.route('/')
def index():
    stroka = '<pre>'
    for i in data:
        stroka += f"{i} \n\n"
    stroka += '</pre>'
    return stroka


@app.route("/candidates/<int:pk>")
def get_user(pk):
    user = get_by_pk(pk, data)
    if user:
        stroka = f"<img src = '{user.picture}'></img>"
        stroka += f'<pre> {user} </pre>'
    else:
        stroka = "NOT FOUND"
    return stroka


@app.route("/skills/<x>")
def get_users(x):
    x = x.lower()
    users = get_by_skill(x, data)
    if users:
        stroka = '<pre>'
        for i in users:
            stroka += f"{i} \n\n"
        stroka += '</pre>'
    else:
        stroka = "NOT FOUND"
    return stroka


if __name__ == '__main__':
    app.run(port=5000, debug=True)
