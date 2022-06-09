"""Server for Melon Tasting App"""

from flask import Flask, render_template, session, flash
from jinja2 import StrictUndefined
import os

from model import connect_to_db


app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined

app.secret_key = os.environ['FLASK_SECRET_KEY']


### Routes ###
@app.route("/")
def show_homepage():
    """Return homepage"""

    return render_template("index.html")


if __name__ == "__main__":

    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)