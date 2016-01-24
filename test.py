from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
def page1():
	return render_template('page1.html')

@app.route('/page2', methods=['GET', 'PAGE2'])
def page2():
	if request.method == 'page2':

		return redirect(url_for('page1.html'))


	return render_template('page2.html')


if __name__ == '__main__':

	app.run()