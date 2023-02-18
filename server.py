from flask import Flask, url_for, request, render_template, redirect
import json
from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError
# Большинство из этих импортов могут быть не нужны именно в этой задаче, 
# но для удобства они все равно добавлены

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kLxEZ8<_q[5$%N#Z'

EDUCATION_TYPES = [
    "Никакое",
    "none",
    "Базовое",
    "Основное",
    "Специальное",
    "Высшее"
]

GENDERS = [
    "Муж", "Мужчина", "Парень", "м", "male",
    "Жен", "Женщина", "Девушка", "ж", "female",
    "не определился"
]


def education_validation(form, field):
    if field.data not in EDUCATION_TYPES:
        raise ValidationError("Такого образования нет")

def gender_validator(form, field):
    if field.data not in GENDERS:
        raise ValidationError("На борьбу с мутантами мутантов не берут.")

class MissionForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    education = StringField('Образование', validators=[DataRequired(), education_validation])
    profession = StringField('Профессия', validators=[])
    gender = StringField('Пол', validators=[DataRequired(), gender_validator])
    motivation = StringField('Опишите, почему вы хотите попасть к нам', validators=[DataRequired()])
    allowance = BooleanField('Готовы остаться на марсе?', validators=[DataRequired(message="Без вашего согласия вас не получится запихнуть на вечно на марс. МУХАХАХАХАХАХХАХ")])
    submit = SubmitField('Записаться')


@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html', title="Home")


@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    if 'инженер' in str(prof) or 'строитель' in str(prof):
        param['prof'] = True
    else:
        param['prof'] = False
    return render_template('trainer.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MissionForm()
    if form.validate_on_submit():
        return redirect('/home')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/list_prof/<list>')
def professions(list):
    param = {}
    with open("jobs.json", "rt", encoding="utf8") as f:
        profs = json.loads(f.read())
    if list == 'ul':
        param['list_type'] = "ul"
    elif list == 'ol':
        param['list_type'] = "ol"
    else:
        return render_template('wrong_param.html')
    return render_template('professions.html', prof=profs, **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
