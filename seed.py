"""Script to seed database"""

import os, model, server

# Reset db
os.system("dropdb melontasting")
os.system("createdb melontasting")

# Connect to db
model.connect_to_db(server.app)

# Create db tables
model.db.create_all()


# Create a 2 fake users
usernames = ["harperlee", "rupikaur"]

for username in usernames:

    new_user = model.User.create_user(username)
    model.db.session.add(new_user)

model.db.session.commit()


# Create a few fake reservations
datetime_str = ["02/14/2023 05:30 PM",
                "05/14/2023 11:00 AM",
                "11/11/2023 06:00 PM",
                "12/18/2023 07:30 PM"
]

users_id = []

users_db = model.User.get_users()

for user in users_db:
    users_id.append(user.user_id)

new_reservations = []

j = 0 

for user_id in users_id:

    for n in range(2):
        reservation = model.Reservation.create_reservation(user_id, datetime_str[j])
        new_reservations.append(reservation)

        j += 1

model.db.session.add_all(new_reservations)
model.db.session.commit()