from app import app, db, login_manager
from app.models import Book,Order,OrderItem,Cart,User,Promotion,AppliedPromotion

from flask_mail import Message
from app import mail

def reorder(bookID,amount):
    book = Book.query.get(bookID)
    bk = Book.query.filter(Book.bookID==book.bookID).first()
    bk.stock = Book.stock + amount
    subject = "Order"

    message = "Thank You"
    msg = Message(subject, sender = 'order@becky.com', recipients = ["manager@becky.com"])
    msg.body = str(amount) + "Books Have Been Reordered"
    mail.send(msg)
    


def checkStock():
    books = db.session.query(Book).all()

    for book in books:
        if not book.stoporder and book.stock <= book.reorderthres:
            reorder(book.bookID,30)
