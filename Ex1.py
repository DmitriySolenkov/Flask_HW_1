from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/boots/')
def boots():
    return render_template('boots.html')


@app.route('/coats/')
def coats():
    return render_template('coats.html')


if __name__ == '__main__':
    app.run(debug=True)
