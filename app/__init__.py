from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a super secure key"  # you should make this more random and unique
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:rootpassword@127.0.0.1/becky"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # necessary to tell Flask-Login what the default route is for the login page
login_manager.login_message_category = "info"  # customize the flash message category

app.config.from_object(__name__)

#Flask Mail
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'f38e46d0dcc254'
app.config['MAIL_PASSWORD'] = '5f6b8858994448'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

from app import views
