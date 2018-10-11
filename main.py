from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField
from flask import render_template, session, redirect, url_for
import flask

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = 'secret'
app.debug = True


class someForm(FlaskForm):
	
	name = StringField('First Name', 
		[validators.InputRequired(), 
		validators.Length(min = 1, max = 30, message = "First name must be between 1-30 chars")])

	lname = StringField('Last Name', 
		[validators.InputRequired(), 
		validators.Length(min = 1, max = 30, message = "Last name must be between 1-30 chars")])

	email = EmailField('Email', 
		[validators.InputRequired(), 
		validators.Email(message = "Email needs to be valid.")])

	username = StringField('Username', 
		[validators.InputRequired(), 
		validators.Length(min = 6, max = 20, message = "Username must be between 6-20 chars")])

	password = PasswordField('Password', 
		[validators.InputRequired(), 
		validators.Length(min = 6, max = 20, message = "Password must be between 6-20 chars")])


@app.route('/', methods = ['GET','POST'])
def someform():
	
	form = someForm()

	if form.validate_on_submit():
		print("validated!")
		return redirect(url_for('success'))


	return render_template('someform.html', form = form)


@app.route('/success')
def success():
	return "<h1>Success!!</h1>"

if __name__ == "__main__":
	app.run()


