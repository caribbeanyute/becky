from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField ,IntegerField, DecimalField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    manager = BooleanField('Manager')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    member = BooleanField('Member')

class Promotion(FlaskForm):
    pass


class BookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    price = DecimalField('price', validators=[DataRequired()])
    stock = IntegerField('stock', validators=[DataRequired()])
    reorderthres = IntegerField('reorderthres', validators=[DataRequired()])
    