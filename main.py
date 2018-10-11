from flask import render_template, session, redirect, url_for
import flask
from theforms import someForm

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = 'secret'
app.debug = True

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


