from . import db
from werkzeug.security import generate_password_hash
import datetime


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


        





class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    pwd_hash = db.Column(db.String(200))
    email = db.Column(db.String(256),unique=True)
    is_active = db.Column(db.Boolean,default=False)
    urole = db.Column(db.String(80))
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    member = db.Column(db.Boolean, nullable=False)


    def __init__(self,username,password,email,name,address,is_member=False,urole="cust"):
        self.username = username
        self.pwd_hash = generate_password_hash(password, method='pbkdf2:sha256')
        self.email = email
        self.urole = urole
        self.name = name
        self.email = email
        self.address = address
        self.member = True
        

    def get_id(self):
            return self.id
    def is_active(self):
            #return self.is_active
            return True
    def is_authenticated(self):
        return True

    def activate_user(self):
            self.is_active = True         
    def get_username(self):
            return self.username
    def get_urole(self):
            return self.urole
    def __repr__(self):
        return '<User %r>' %  self.username


class Order(db.Model):
    __tablename__ = 'order'

    ordID = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))
    cust = db.Column(db.String(255), nullable=False)

    def __init__(self,cust):
        self.cust = cust


class OrderItem(db.Model):
    __tablename__ = 'items'

    itID = db.Column(db.Integer, primary_key=True)
    ordID = db.Column(db.ForeignKey('order.ordID'), nullable=False, index=True)
    bookID = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(asdecimal=True), nullable=False)

    order = db.relationship('Order')

    def __init__(self,ordID,bookID,title,author,price):
        self.ordID = ordID
        self.bookID = bookID
        self.title = title
        self.author = author
        self.price = price



class Promotion(db.Model):
    __tablename__ = 'promotions'
    pID = db.Column(db.Integer,primary_key=True)
    promoCode = db.Column(db.String(25))
    percoff = db.Column(db.Float(asdecimal=True), nullable=False)
    expDate = db.Column(db.DateTime)
    def __init__(self,promoCode,percoff,expDate):
        self.promoCode = promoCode
        self.percoff = percoff
        self.expDate = datetime.datetime.strptime(expDate, '%d/%m/%Y')


class Cart(db.Model):
    __tablename__ = 'cart'

    cID = db.Column(db.Integer, primary_key=True)
    custID = db.Column(db.Integer)
    bookID = db.Column(db.Integer)
    def __init__(self,custID,bookID):
        self.custID = custID
        self.bookID = bookID

class AppliedPromotion(db.Model):
    __tablename__ = 'appliedpromotions'
    apID = db.Column(db.Integer, primary_key=True)
    pID = db.Column(db.Integer)
    cID = db.Column(db.Integer)
    def __init__(self,pID,cID):
        self.pID = pID
        self.cID = cID
