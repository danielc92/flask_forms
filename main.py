from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import ValidationError
from wtforms.fields.html5 import EmailField
from flask import render_template, session, redirect, url_for
import flask
import string

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = 'secret'
app.debug = True


def checkName(form, field):

	allowable = string.ascii_letters

	for char in field.data:
		if char not in allowable:
			raise ValidationError('Name must contain alphabet characters only.')

def checkUsername(form, field):

	allowable = string.ascii_letters + string.digits + '_'

	for char in field.data:
		if char not in allowable:
			raise ValidationError("Username can contain a-z, A-Z, 0-9 and '_' only.")

def checkPassword(form, field):

	allowable = string.ascii_letters + string.digits + '@#$!%^&*'

	for char in field.data:
		if char not in allowable:
			raise ValidationError("Passwords can contain a-z, A-Z, 0-9 and '!@#$%^&*' only.")


class someForm(FlaskForm):
	
	name = StringField('First Name', 
		[validators.InputRequired(), 
		validators.Length(min = 1, max = 30, message = "First name must be between 1-30 chars."),
		checkName])

	lname = StringField('Last Name', 
		[validators.InputRequired(), 
		validators.Length(min = 1, max = 30, message = "Last name must be between 1-30 chars."),
		checkName])

	email = EmailField('Email', 
		[validators.InputRequired(), 
		validators.Email(message = "Email is invalid, try again.")])

	username = StringField('Username', 
		[validators.InputRequired(), 
		validators.Length(min = 6, max = 20, message = "Username must be between 6-20 chars."),
		checkUsername])

	password = PasswordField('Password', 
		[validators.InputRequired(), 
		validators.Length(min = 6, max = 20, message = "Password must be between 6-20 chars."),
		checkPassword])

	confirm_password = PasswordField('Confirm Password',
		[validators.InputRequired(),
		validators.EqualTo('password', message = "Passwords have to match dude.")])


@app.route('/', methods = ['GET','POST'])
def someform():
	
	form = someForm()

	if form.validate_on_submit():

		return redirect(url_for('success'))


	return render_template('someform.html', form = form)


@app.route('/success')
def success():
	return "<h1>Success!!</h1>"

if __name__ == "__main__":
	app.run()


