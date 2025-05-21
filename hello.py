from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)

# Create a route decorator
# @app.route('/')
# def index():
# 	return "<h1>Hello World!</h1>"

@app.route('/')
def index():
	f_name = "Virinchi"
	stuff = "this is bold text"
	favorite_pizza = ["pepperoni", "Cheese", "Mushrooms", 41]
	return render_template('index.html', first_name=f_name, htmlStuff=stuff, favt_pizza = favorite_pizza)


# localhost:5000/user/John
@app.route('/users/<name>')
def user(name):
	return render_template('user.html', user_name=name)

# Create Custom Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500