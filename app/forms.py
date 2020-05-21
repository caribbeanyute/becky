from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField ,IntegerField, DecimalField, DateField
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

class PromotionForm(FlaskForm):
    promocode = StringField("Promotion Code",validators=[DataRequired()])
    expDate = StringField("Expiry Date",validators=[DataRequired()])
    percentageOff= DecimalField('Percentage Discount', validators=[DataRequired()])

class ApplyPromotionForm(FlaskForm):
    promocode = StringField("Promotion Code",validators=[DataRequired()])


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author(s)', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired()])
    reorderthres = IntegerField('Reorder Threshold', validators=[DataRequired()])
    stoporder = BooleanField('Stop Order')


class PaymentForm(FlaskForm):
    credit = StringField("Credit Card",validators=[DataRequired()])
