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
datetime_str = ["2022-03-01 11:30",
                "2022-04-14 14:00",
                "2022-05-20 15:30",
                "2022-06-23 11:30"
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


# Create open reservation slots
slots_str = ["11:00",
            "11:30",
            "13:00",
            "13:30",
            "14:00",
            "14:30",
            "15:00",
            ]

open_slots = []

for i in range(1, 32):
    for slot in slots_str:
        if i < 10:
            slot_str = f"2022-08-0{i} {slot}"
        else:
            slot_str = f"2022-08-{i} {slot}"
        
        new_slot = model.OpenSlots.create_slot(slot_str)
        open_slots.append(new_slot)

model.db.session.add_all(open_slots)
model.db.session.commit()
