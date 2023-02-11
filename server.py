from flask import Flask, url_for, request, render_template, redirect
import json
from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired
# Большинство из этих импортов могут быть не нужны именно в этой задаче, 
# но для удобства они все равно добавлены

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kLxEZ8<_q[5$%N#Z'


@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')