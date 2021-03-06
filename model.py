"""Models for Melon Tasting App"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)

    # reservations = a list of Reservation objects associated with the user

    def __repr__(self):
        """A string representation of a user"""

        return f"<User user_id={self.user_id} username={self.username}>"
    
    @classmethod
    def create_user(cls, username):
        "Create and return a new user"

        username = username.lower()

        user = cls(username=username)

        db.session.add(user)
        db.session.commit()

        return user
    
    @classmethod
    def get_users(cls):
        """Return all users"""

        return cls.query
    
    @classmethod
    def get_user_by_username(cls, username):
        """Return a user by username"""

        return cls.query.filter(cls.username == username).first()


class Reservation(db.Model):
    """A reservation"""

    __tablename__ = "reservations"

    reservation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    reservation_date = db.Column(db.DateTime)

    user = db.relationship("User", backref="reservations")

    def __repr__(self):
        """A string representation of a reservation"""

        return f"<Reservation reservation_id={self.reservation_id} user={self.user_id} reservation_date={self.reservation_date}>"
    
    @classmethod
    def create_reservation(cls, user_id, datetime_str):
        """Create and return a new reservation"""

        if isinstance(datetime_str, str):
            reservation_date = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        else:
            reservation_date = datetime_str

        reservation = cls(user_id=user_id, reservation_date=reservation_date)

        db.session.add(reservation)
        db.session.commit()

        return reservation
    
    @classmethod
    def get_reservations(cls):
        """Return all reservations"""

        return cls.query
    
    @classmethod
    def delete_reservation(cls, reservation_id):
        """Delete reservation from db"""

        reservation = cls.query.filter_by(reservation_id=reservation_id).first()

        db.session.delete(reservation)
        db.session.commit()


class OpenSlots(db.Model):
    """An open reservation slot"""

    __tablename__ = "slots"

    slot_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    slot_datetime = db.Column(db.DateTime)

    def __repr__(self):
        """A string representation of an open slot"""

        return f"<OpenSlot slot={self.slot_id} slot_datetime={self.slot_datetime}>"
    
    @classmethod
    def create_slot(cls, slot_datetime_str):
        """Create and return a new open slot"""

        if isinstance(slot_datetime_str, str):
            slot_datetime = datetime.strptime(slot_datetime_str, "%Y-%m-%d %H:%M")

        slot = cls(slot_datetime=slot_datetime)

        db.session.add(slot)
        db.session.commit()

        return slot
    
    @classmethod
    def get_open_slots(cls):
        """Return all open slots"""

        return cls.query
    
    @classmethod
    def get_slot_by_id(cls, slot_id):
        """Return a slot by id"""

        return cls.query.filter(cls.slot_id == slot_id).first()
    
    @classmethod
    def delete_slot(cls, slot_id):
        """Delete slot from open slot table"""

        slot = cls.query.filter_by(slot_id=slot_id).first()

        db.session.delete(slot)
        db.session.commit()


def connect_to_db(flask_app, db_uri="postgresql://sogrnwmdkxrrjh:e6a06655cc03773d8a6e5cd952af5bab1030a3e845e46a2758ed11592bb3ba08@ec2-107-22-238-112.compute-1.amazonaws.com:5432/dcjhbnd6ettst1", echo=True):
    """Connect Flask app to database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri    
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False                      

    db.app = flask_app
    db.init_app(flask_app)                                         

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)