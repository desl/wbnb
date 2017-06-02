# wearbnb
[https://wbnb.herokuapp.com/](https://wbnb.herokuapp.com/)

* do your laundry at someone else's house
* host someone for laundry and get paid

## So what does it do?

You've got laundry to do, but the laundromat is a drag.
Take a look at people near you who for a few bucks will open up their laundry rooms for you to visit.

Or maybe you're going to watch the game anyway. Why not make a few bucks while entertaining a fellow sportsfan while they wash and fold.

This app connects these two people to hang out and get some laundry done.

Try it out: [https://wbnb.herokuapp.com/](https://wbnb.herokuapp.com/)

## If I had more time...

Here's what I'd do if I had more time.

* render a map to see wearbnbs
* tests
* notification email when someone joins or leaves a wearbnb
* account deletion
* handle payments
* skim a little from those payments

## Technologies Used

#### Languages

* Javascript
* Python
* Jquery
* AJAX
* SQL
* Postgress

#### With the following libraries

* Flask
	* flask-login
	* flask-modus
	* flask-wtf
	* flask-blueprints
	* flask-sqlalchemy
	* flask-migrate
* Geocoder
* Twitter Bootstrap
* bcrypt

## Deployment

#### Get it up and running locally
###### Assumes a unix-like or mac environment

1. Clone the repo: ```git clone https://github.com/desl/wbnb```
2. ```cd wbnb```
3. Highly recommend: ```mkvirtualenv wbnb```
4. ```pip install -r requirements.txt```
3. Assuming postgres is already installed ```createdb wbnb```
4. Do the database migration/upgrade: ```python manage.py db upgrade```
5. Start the server: ```python app.py```
6. Runs on port 3000. [http://localhost:3000/](http://localhost:3000/)