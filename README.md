# wearbnb
###### do your laundry at someone else's house
###### host someone for laundry and get paid

## So what does it do?

You've got laundry to do, but the laundromat is such a drag.
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

Uses the following technologies

* Flask
	* flask-login
	* flask-modus
	* flask-wtf
	* flask-blueprints
	* flask-sqlalchemy
	* flask-migrate
* Postgres
* jquery
* ajax
* Twitter Bootstrap
* geocoder python library

## Deployment
###### App is deployed to heroku

1. get yourself a heroku account.
	* set up the app with a postrgres database.
2. clone the repo
3. Create a heroku remote
3. push it to heroku: git push heroku master
4. *do the database upgrade* python manage.py db upgrade