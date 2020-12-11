from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		a = request.json['text']
		return a
	return '<h1> s.a aq </h1>'
if __name__ == '__main__':
	app.run(debug=True)
