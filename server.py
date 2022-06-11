"""Server for Melon Tasting App"""

from flask import Flask, render_template, request, redirect, session, flash, jsonify
from jinja2 import StrictUndefined
import os

from model import connect_to_db, User, OpenSlots, Reservation

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

@app.route("/signup/<slot_id>")
def sign_up(slot_id):
    """Sign up a user for an open reservation slot"""

    slot = OpenSlots.get_slot_by_id(slot_id)

    # Get the datetime object for the open slot
    slot_datetime = slot.slot_datetime

    # Convert into a string
    slot_datetime_str = slot_datetime.strftime("%Y-%m-%d")

    user = User.get_user_by_username(session["username"])

    reservations = user.reservations

    for reservation in reservations:

        res_datetime = reservation.reservation_date
        res_datetime_str = res_datetime.strftime("%Y-%m-%d")

        if slot_datetime_str == res_datetime_str:
            flash("Limit of one tasting per date! Please select another date.")
            
            return redirect("/")

    # Add the reservation to the user's reservations
    Reservation.create_reservation(user.user_id, slot_datetime)

    # Delete the slot from the availability page
    OpenSlots.delete_slot(slot_id)
    
    flash("Reservation added! We look forward to seeing you soon.")

    return redirect("/")

@app.route("/delete/<reservation_id>")
def delete_reservation(reservation_id):
    """Sign up a user for an open reservation slot"""

    Reservation.delete_reservation(reservation_id)
    
    flash("Reservation deleted! We hope to see you soon.")

    return redirect("/")


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

        str_date = res_datetime.strftime("%-m/%-d/%Y")

        str_time = res_datetime.strftime("%-I:%M %p")

        db_reservations[i] = {"reservation_id": reservation.reservation_id,
                            "user_id": reservation.user_id,
                            "date": str_date,
                            "time": str_time
        }

    return jsonify(db_reservations)

@app.route("/api/slots", methods=["POST"])
def search_reservations():
    """Return available reservation slots"""

    date = request.json.get("date")

    # # For Version 2.0:
    # start = request.json.get("start")
    # end = request.json.get("end")

    # if start != "" and end == "":
    #     flash("You selected a start time but no end time! Please try again.")
    #     return redirect("/")
    # elif start == "" and end != "":
    #     flash("You selected an end time but no start time! Please try again.")
    #     return redirect("/")
    # elif start == "" and end == "":
    #     date_str = datetime.strptime(date, "%Y-%m-%d %H:%M")

    # else:
    #     date_start_str = 


    slots = OpenSlots.get_open_slots().all()

    db_available = {}

    for i, slot in enumerate(slots):

        slot_datetime = slot.slot_datetime

        str_date = slot_datetime.strftime("%Y-%m-%d")

        if str_date == date:

            str_date = slot_datetime.strftime("%-m/%-d/%Y")

            str_time = slot_datetime.strftime("%-I:%M %p")

            db_available[i] = {"slot_id": slot.slot_id,
                                "date": str_date,
                                "time": str_time
            }

    return jsonify(db_available)



if __name__ == "__main__":

    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)