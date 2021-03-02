from flask import Flask, render_template, request
from handlers.pulls import get_pulls
import requests
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/pulls')
def pulls():
    headers = {'Authorization': 'token %s' % "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
               'per_page': 100,
               'state': 'all'}
    r = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls', params=headers)
    rj = r.json()
    state = request.args.get("state")
    return render_template("pulls.j2", pulls=get_pulls(state, rj))


app.run()
