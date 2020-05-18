"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, jsonify, make_response, json
from flask_login import login_user, logout_user, current_user, login_required
from app.models import Book,Order,OrderItem,Cart,User,Promotion,AppliedPromotion
from werkzeug.security import check_password_hash,generate_password_hash

from app.forms import LoginForm,RegisterForm,BookForm,PromotionForm,ApplyPromotionForm,PaymentForm

from flask_mail import Message
from app import mail



@app.route('/')
def home():
    """Render website's home page."""
    #print(render_template('home.html'))
    return render_template('home.html')


@app.route('/about')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")



@app.route('/secure-page')
@login_required
def secure_page():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('secure_page.html')



# Sec fix never excute uncleant sql
@app.route('/books')
def get_books():
    books = db.session.query(Book).order_by(Book.title.asc()).all()
    
    return render_template('books.html', books=books)

@app.route('/cart')
def cart():
    print(current_user.id)


    total=0
    books = db.session.query(Book).join(Cart, Book.bookID==Cart.bookID).filter(Cart.custID==current_user.id)
    for book in books:
        total += book.price
    
    return render_template('cart.html',total=total,books=books)

@app.route('/cart/addBook/<bookid>',methods=['POST'])
def addBookCart(bookid):
    if request.method == 'POST':
        cart = Cart(current_user.id,bookid)
        db.session.add(cart)
        db.session.commit()
    return redirect(url_for('cart'))


@app.route('/cart/remBook/<bookid>',methods=['POST'])
def removeBookCart(bookid):
    if request.method == 'POST':
        Cart.query.filter(Cart.custID == current_user.id ).filter(Cart.bookID==bookid).delete()
        db.session.commit()
    return redirect(url_for('cart'))






@app.route('/applyPromotion',methods=['POST','GET'])
def applyPromo():
    appForm = ApplyPromotionForm()
    if request.method == 'POST':
        chk = db.session.query(AppliedPromotion).join(Promotion, AppliedPromotion.pID==Promotion.pID).filter(Promotion.promoCode==appForm.promocode.data).first()
        if chk:
            flash('Promotion Code Already Applied', 'danger')
            return redirect(url_for('checkOut'))
        else:
            cart = Cart.query.filter(Cart.custID == current_user.id ).first()
            promo = Promotion.query.filter(Promotion.promoCode == appForm.promocode.data).first()
            app = AppliedPromotion(promo.pID,cart.cID)
            db.session.add(app)
            db.session.commit()
            return redirect(url_for('checkOut'))
    return render_template('applyPromotion.html',form=appForm)


# Fix for more than one promo to be applied
@app.route('/checkOut',methods=['POST','GET'])
def checkOut():
    cart = Cart.query.filter(Cart.custID == current_user.id ).first()
    
    applied = Promotion.query.join(AppliedPromotion,Promotion.pID==AppliedPromotion.pID).filter(AppliedPromotion.cID==cart.cID).all()
    

    total=0
    books = db.session.query(Book).join(Cart, Book.bookID==Cart.bookID).filter(Cart.custID==current_user.id)
    for book in books:
        total += book.price
    discount, di = 0,0
    for prom in applied:
        di+=1
        discount += prom.percoff
    print(discount,di)
    total = total * (1-(discount/(di*100)))
        
    
    return render_template('checkout.html',total=total,books=books,applied=applied)


@app.route('/order')
def ordr():
    cart = Cart.query.filter(Cart.custID == current_user.id ).first()
    
    applied = Promotion.query.join(AppliedPromotion,Promotion.pID==AppliedPromotion.pID).filter(AppliedPromotion.cID==cart.cID).all()
    

    total=0
    books = db.session.query(Book).join(Cart, Book.bookID==Cart.bookID).filter(Cart.custID==current_user.id)
    for book in books:
        total += book.price
    subtotal = total
    discount, di = 0,0
    for prom in applied:
        di+=1
        discount += prom.percoff
    print(discount,di)
    total = total * (1-(discount/(di*100)))
    user = User.query.get(current_user.id )
    return render_template('order/order.html',user=user,books=books,app=applied,subtotal=subtotal,total=total,discount=discount)
    
    



@app.route('/purchase',methods=['GET','POST'])
def purchase():
    form = PaymentForm()
    user = User.query.filter(User.id==current_user.id).first()
    cart = Cart.query.filter(Cart.custID == current_user.id ).all()

    

    if request.method == 'POST' and form.validate_on_submit():
        order = Order(user.username)
        db.session.add(order)
        db.session.commit()
        books = db.session.query(Book).join(Cart,Book.bookID==Cart.bookID).filter(Cart.custID==current_user.id).all()
        for book in books:
            #Removing  book from stock
            bk = Book.query.filter(Book.bookID==book.bookID).first()
            bk.stock = Book.stock - 1

            # Recording Sale
            orderIt = OrderItem(order.ordID,book.bookID,book.title,book.author,book.price)
            db.session.add(orderIt)
            



        #Clearing Cart and Promo
        subject = "Order"
        message = "Thank You"
        msg = Message(subject, sender = 'order@becky.com', recipients = [user.email])
        msg.body = message
        msg.html = ordr()
        mail.send(msg)



    db.session.commit()


    return render_template("payment.html",form=form)




@app.route('/register', methods=['POST','GET'])
def register():
    form = RegisterForm()
    # Login and validate the user.
    if request.method == 'POST' and form.validate_on_submit():
        # Query our database to see if the username and password entered
        # match a user that is in the database.
        username = form.username.data
        password = form.password.data
        name = form.name.data
        address = form.address.data
        email = form.email.data
        
        new_user = User(username=username,name=name, password=password,email=email, address=address)
        db.session.add(new_user)
        db.session.commit()
    
    return render_template('register.html', form=form)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # if user is already logged in, just redirect them to our secure page
        # or some other page like a dashboard
        return redirect(url_for('secure_page'))

    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    # Login and validate the user.
    if request.method == 'POST' and form.validate_on_submit():
        # Query our database to see if the username and password entered
        # match a user that is in the database.
        username = form.username.data
        password = form.password.data
        isManager = form.manager.data

        # user = UserProfile.query.filter_by(username=username, password=password)\
        # .first()
        # or
        
        user = User.query.filter_by(username=username).first()

        if user is not None and check_password_hash(user.pwd_hash, password):
            remember_me = False

            if 'remember_me' in request.form:
                remember_me = True

            # If the user is not blank, meaning if a user was actually found,
            # then login the user and create the user session.
            # user should be an instance of your `User` class
            login_user(user, remember=remember_me)

            flash('Logged in successfully.', 'success')

            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            flash('Username or Password is incorrect.', 'danger')

    flash_errors(form)
    return render_template('login.html', form=form)



@app.route("/logout")
@login_required
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))


# This callback is used to reload the user object from the user ID stored in the session.
# It should take the unicode ID of a user, and return the corresponding user object.
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))




 ## For Mnanager


@app.route('/addBook', methods=['GET','POST'])
def add_book():
    form = BookForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_Book = Book(form.title.data, form.author.data, form.price.data, form.reorderthres.data,  form.stock.data)
        db.session.add(new_Book)
        db.session.commit()
        return redirect(url_for('get_books'))
    return render_template("add_book.html", form = form)

#FIX
@app.route('/updateBook/<bookid>', methods=['GET','POST'])
def update_book(bookid):
    form = BookForm()
    book = Book.query.get(bookid)
    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(book)
        db.session.commit()
        return redirect(url_for('get_books'))
    return render_template("update_book.html", form = form,book =book)

    
    #new_Book = Book(data['title'], data['author'], data['price'], data['reorderthres'], data['stoporder'], data['stock'])
    db.session.commit()
    
    return render_template("add_book.html", form = form)



@app.route('/addPromotion', methods=['GET','POST'])
def addPromo():
    form = PromotionForm()
    print(form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit():
        promo = Promotion(promoCode=form.promocode.data,percoff=form.percentageOff.data,expDate=form.expDate.data)
        db.session.add(promo)
        db.session.commit()
    return render_template("promotion.html", form = form)




# Flash errors from the form if validation fails with Flask-WTF
# http://flask.pocoo.org/snippets/12/
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response



@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
