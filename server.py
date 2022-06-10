"""Server for Melon Tasting App"""

from flask import Flask, render_template, request, redirect, session, flash, jsonify
from jinja2 import StrictUndefined
import os

from model import connect_to_db, User

from datetime import datetime


app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined

app.secret_key = os.environ['FLASK_SECRET_KEY']


### Standard Routes ###

@app.route("/")
def show_homepage():
    """Return homepage"""

    return render_template("index.html")

@app.route("/login", methods=["POST"])
def process_login():
    """Log user into app"""

    username = request.form.get("username")
    user = User.get_user_by_username(username)

    if user:
        session["username"] = username
        flash(f"Success! Welcome back to Il Dolce Melone, {username}!")
    else:
        flash("Username does not exist! Please try again.")
    
    return redirect("/")

@app.route("/logout")
def process_logout():
    """Delete session and logout user"""

    session["username"] = None

    flash("You have been logged out.")

    return redirect("/")

@app.route("/search", methods=["POST"])
def search_reservations():
    """Return available reservation slots"""

    date = request.form.get("date")
    start = request.form.get("start")
    end = request.form.get("end")

    # if start != "" and end == "":
    #     flash("You selected a start time but no end time! Please try again.")
    #     return redirect("/")
    # elif start == "" and end != "":
    #     flash("You selected an end time but no start time! Please try again.")
    #     return redirect("/")
    # elif start == "" and end == "":
    #     datetime_str = f"{date} "

    return {"date": date, "start": start, "end": end}


### API Routes ###

@app.route("/api/session_username")
def username_data():
    """JSON information about session username"""

    return jsonify(session["username"])

@app.route("/api/reservations")
def reservations_data():
    """JSON information about a user's reservations"""

    user = User.get_user_by_username(session["username"])
    reservations = user.reservations

    db_reservations = {}

    for i, reservation in enumerate(reservations):

        res_datetime = reservation.reservation_date

        str_date = res_datetime.strftime("%A, %B %-m, %Y")

        str_time = res_datetime.strftime("%-I:%M %p")

        db_reservations[i] = {"reservation_id": reservation.reservation_id,
                            "user_id": reservation.user_id,
                            "date": str_date,
                            "time": str_time
        }

    return jsonify(db_reservations)


if __name__ == "__main__":

    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)