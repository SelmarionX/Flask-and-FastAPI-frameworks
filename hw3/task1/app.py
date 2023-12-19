from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from bcrypt import gensalt, hashpw

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


def create_database(app):
    with app.app_context():
        db.create_all()


class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(max=50)])
    surname = StringField('Фамилия', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Зарегистрироваться')


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = hashpw(form.password.data.encode('utf-8'), gensalt())
        new_user = User(name=form.name.data, surname=form.surname.data,
                        email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login')
def login():
    return 'Авторизация прошла успешно!'


if __name__ == '__main__':
    app.run(debug=True)
    create_database(app)
