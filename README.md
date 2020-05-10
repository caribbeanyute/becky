# Becky Bookstore App
The Book E-Commerce System will allow any user to create an account to become a customer. The customer, through the process of account creation, will have the option to become a member of the site. The system will allow customers to browse, search, select, and add books to a shopping cart. Then, provided they have books in their shopping cart, check out books in shopping cart and decrement the stock that the inventory the system maintains. The BECS also allows a manager to manage the inventory with full create, retrieve, update and delete (CRUD) functionality with regards to books in the system. It will also allow, on an inventory wide basis, customers and managers to interact with a promotion system that handles percentage-off promotions that can be applied to member’s orders. This interaction includes the creation (by managers) and the application to orders (by customers) of the promotions. The BECS has full email capabilities; the automated email functionality will be used to send promotions to members of the system as well as provide the managers with low-stock notifications.



## Setup
**Note:** This app uses a MYSQL database along with Flask-SQLAlchemy and Flask-Migrate.

To begin using this app you can do the following:

1. Clone the repository to your local machine or cloud repo
.
2. Create a Python virtual environment e.g. `python -m venv venv` (or `python3 -m venv venv` or `python3.5 -m venv venv` on Cloud 9)
3. Enter the virtual environment using `source venv/bin/activate` (or `.\venv\Scripts\activate` if you are using Windows) 
4. Install the dependencies using Pip. e.g. `pip install -r requirements.txt`. __Note:__ Ensure you have MYSQL already installed and a database created.
5. Edit the `app/__init__.py` file and enter your database credentials and database name.
6. Run the migrations by typing `python flask-migrate.py db upgrade`
7. Ensure you add a user to your database to test the login system.
8. Start the development server using `python run.py`.
