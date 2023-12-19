from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=8),
                                                   Regexp(r'^.*(?=.{8,})(?=.*\d)(?=.*[a-zA-Z]).*$',
                                                          message='Пароль должен содержать не менее 8 символов,'
                                                                  ' включая хотя бы одну букву и одну цифру')])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password',
                                                                                                 message='Пароли должны'
                                                                                                         ' совпадать')])
    submit = SubmitField('Зарегистрироваться')
