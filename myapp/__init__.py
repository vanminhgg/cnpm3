from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= "mysql+pymysql://root:12345678@localhost:3306/phongkham?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = "!@#$%^&*()_+"
db = SQLAlchemy(app=app)
admin = Admin(app=app, name="PHONG KHAM", template_mode="bootstrap4")
my_login = LoginManager(app=app)