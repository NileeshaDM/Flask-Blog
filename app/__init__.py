from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__) #The __name__ variable passed to the Flask class is a Python predefined variable
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login' # If a user who is not logged in tries to view a protected page, Flask-Login will automatically redirect the user to the login form, and only redirect back

from app import routes, models # The routes handle the different URLs that the application supports.