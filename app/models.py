from . import db
from werkzeug.security import generate_password_hash


class Book(db.Model):
    __tablename__ = 'book'

    bookID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(asdecimal=True), nullable=False)
    reorderthres = db.Column(db.Integer, nullable=False)
    stoporder = db.Column(db.Boolean, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, title, author, price, reorderthres, stock):
        self.title=title
        self.author=author
        self.price = price
        self.reorderthres = reorderthres
        self.stoporder = False
        self.stock = stock

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


        


class Customer(db.Model):
    __tablename__ = 'customer'

    custID = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(255), nullable=False)
    passwordHash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    member = db.Column(db.Boolean, nullable=False)

    def __init__(self, public_id, username, password, name, email, address):
        self.username = username
        self.public_id = public_id
        self.passwordHash = generate_password_hash(password, method='pbkdf2:sha256')
        self.name = name
        self.email = email
        self.address = address
        self.member = True
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.username



class Manager(db.Model):
    __tablename__ = 'manager'

    manID = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(255), nullable=False)
    passwordHash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    def __init__(self, username, password, name, email):
        self.username = username
        self.passwordHash = generate_password_hash(password, method='pbkdf2:sha256')
        self.name = name
        self.email = email



class Order(db.Model):
    __tablename__ = 'order'

    ordID = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))
    cust = db.Column(db.String(255), nullable=False)


class Item(db.Model):
    __tablename__ = 'items'

    itID = db.Column(db.Integer, primary_key=True)
    ordID = db.Column(db.ForeignKey('order.ordID'), nullable=False, index=True)
    bookID = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(asdecimal=True), nullable=False)

    order = db.relationship('Order')



class Promotion(db.Model):
    __tablename__ = 'promotions'

    pID = db.Column(db.Integer, primary_key=True)
    percoff = db.Column(db.Float(asdecimal=True), nullable=False)
