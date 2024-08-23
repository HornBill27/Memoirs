from flask import Flask, render_template

#Create a Flask instance
app = Flask(__name__)

#Create a Flask route
@app.route('/')

def index():
	firstName = "John"
	stuff = 'This is <strong>Bold</strong> text'
	favorite_pizza = ['Pepperoni', 'Cabbage', 'Blaze', 41]
	return render_template('index.html',
		first_name = firstName,
		stuff = stuff,
		favorite_pizza = favorite_pizza)



@app.route('/user/<name>')

def user(name):
	return render_template('user.html', user_name=name)


# Create Custom Error Pages

@app.errorhandler(404)

def page_not_found(e):
	return render_template('404.html'), 404


@app.errorhandler(500)

def page_not_found(e):
	return render_template('500.html'), 500
