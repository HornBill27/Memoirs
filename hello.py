from flask import Flask, render_template


# Create a Flask instance
app = Flask(__name__)

# Creating flask routes
@app.route('/')
# FILTERS

# safe
# striptags
# upper
# lower
# title
# capitalize
# trim

def index():
	first_name="virinchi"
	stuff = "This is <strong>Bold</strong> text."
	favorite_pizza = ["Pepperoni", "CheeseCream", "Mushroom", 41]
	return render_template("index.html",
	 first_name=first_name,
	 stuff=stuff,
	 favorite_pizza=favorite_pizza)

@app.route('/user/<name>')

def user(name):
	return render_template('user.html', user_name=name)


# Creating custom error pages
@app.errorhandler(404)

def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)

def server_error(e):
	return render_template("500.html"), 500