# **Melon Tasting Reservation Scheduler**
Now deployed on Heroku: https://tasting-scheduler.herokuapp.com/

A single-page React application that allows users to conveniently search for melon tasting reservations. Saved reservations are persistently stored in PostgreSQL. 

## **Table of Contents**)
* [Design](https://github.com/lunaxlam/melontasting-app#design) 
* [Tech Stack](https://github.com/lunaxlam/melontasting-app#tech-stack) 
* [Features](https://github.com/lunaxlam/melontasting-app#features)
* [Installation](https://github.com/lunaxlam/melontasting-app#installation)
* [Version 2.0](https://github.com/lunaxlam/melontasting-app#version-20)

## **Design**
I selected a single page application design for this project to deliver a seamless experience for the end user. Rather than needing to refresh the entire page any time that data is transmitted, a single page application allows for targeted portions of a webpage to update as asynchronous requests are made.

I used PostgreSQL to structure relational data about users, reservations, and available reservation slots.

## **Tech Stack**
Backend: Flask, Python, PostgreSQL, SQLAlchemy ORM<br />
Frontend: CSS 3, HTML5, JavaScript, Jinja, ReactJS<br/> 

## **Features**
### Account Authentication
Returning users are able to login by entering their username.

<img src="/static/img/site-nav/login.png">

### Search and Add New Reservation
Users are able to select a date to look up available reservation slots.

<img src="/static/img/site-nav/search.png">

Users are then able to sign-up for the open reservation slot.

<img src="/static/img/site-nav/results.png">

### Validate for Same Day Reservations
Users are prevented from signing up for more than one reservation per day, which is indicated by a flash alert.

<img src="/static/img/site-nav/alert.png">

### View and Delete Saved Reservations
Users are able to view and delete previously saved reservations.

<img src="/static/img/site-nav/saved.png">


## **Installation**
Clone or fork the [repository](https://github.com/lunaxlam/melontasting-app.git):

```
https://github.com/lunaxlam/melontasting-app.git
```

In the project directory, create and activate a virtual environment:
```
virtualenv env
source env/bin/activate
```

Install the project dependencies:
```
pip3 install -r requirements.txt
```

Create and save your Flask secret key in a file called <kbd>secrets.sh</kbd> in the following format:
```
export FLASK_SECRET_KEY="YOUR_KEY_HERE"
```

Source your secret key:
```
source secrets.sh
```

Seed the database:
```
python3 seed.py
```

Run the application:
```
python3 server.py
```

In your web browser, navigate to:
```
localhost:5000/
```

## **Version 2.0**
* Enable users to search for new reservations with optional start and end time range filter
* Enable new user sign-up
* Enable password requirement for login
* Unit tests
