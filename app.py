from flask import Flask,render_template
from database import get_data

app =  Flask(__name__)

@app.route('/index')
def index():
    data = get_data()
    return render_template('index.html', data=data)


@app.route('/about')
def about():
    data = get_data()
    return render_template('about.html', data=data)

@app.route('/hil')
def hil():
    return render_template('hil.html')


if __name__=="main":
    app.run()