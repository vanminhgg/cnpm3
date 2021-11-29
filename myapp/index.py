import hashlib
from datetime import datetime
from datetime import date
from myapp import utils

from flask import render_template, request, redirect
from myapp import app, my_login
from flask_login import login_user, logout_user
from myapp.models import Users
from admin import *


@app.route("/")
def home():
    return render_template("home.html")


@my_login.user_loader
def user_load(user_id):
    return Users.query.get(user_id)


@app.route("/login", methods=['post'])
def admin_login():
    username = request.form.get("username")
    password = request.form.get("password")
    users = Users.query.filter(Users.Username == username,
                                   Users.Password == password).first()
    if users:
        login_user(users)

    return redirect("/admin")


@app.route("/user-login", methods=['post', 'get'])
def user_login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        users = Users.query.filter(Users.Username == username,
                                   Users.Password == password).first()
        if users:
            login_user(users)
            return redirect(request.args.get("next", "/"))

    return render_template("user-login.html")


@app.route("/register", methods=['get', 'post'])
def register():
    err_msg = ""
    if request.method == 'POST':
        try:
            password = request.form["Password"]
            confirm_password = request.form['confirm-password']
            if password.strip() == confirm_password.strip():

                data = request.form.copy()
                del data['confirm-password']

                if utils.add_user(**data):
                    return redirect("/user-login")
                else:
                    err_msg = "Du lieu dau vao khong hop le!"
            else:
                err_msg = "Mat khau khong khop!"
        except:
            err_msg = "He thong dang co loi! Vui long quay lai sau!"

    return render_template('register.html', err_msg=err_msg)


@app.route("/user-logout")
def normal_user_logout():
    logout_user()

    return redirect("/user-login")


@app.route("/list-kham")
def list_kham_benh(date=date.today()):
    danhsachkham = utils.get_list_kham(date)
    return  render_template("list-kham.html", danhsachkham=danhsachkham)



@app.route("/add-list-kham", methods=['get', 'post'])
def add_list_kham():
    err_msg = ""
    if request.method == 'POST':
        try:
            data = request.form.copy()
            if utils.add_list_kham(**data):
                return redirect("/list-kham")
            else:
                err_msg = "Du lieu dau vao khong hop le!"
        except:
            err_msg = "He thong dang co loi! Vui long quay lai sau!"
    return render_template("add-list-kham.html", err_msg=err_msg)


@app.route("/add-phieu-kham", methods=['get', 'post'])
def add_phieu_kham():
    err_msg = ""
    if request.method == 'POST':
        try:
            data = request.form.copy()
            if utils.add_phieu_kham(**data):
                return redirect("/list-kham")
            else:
                err_msg = "Du lieu dau vao khong hop le!"
        except:
            err_msg = "He thong dang co loi! Vui long quay lai sau!"
    return render_template("add-phieu-kham.html", err_msg=err_msg)


@app.route("/list-patient")
def list_patient():
    patient = utils.get_patient()
    return  render_template("patient.html", patient=patient)



@app.route("/add-hoa-don", methods=['get', 'post'])
def add_hoadon():
    err_msg = ""
    if request.method == 'POST':
        try:
            data = request.form.copy()
            if utils.add_hoadon(**data):
                return redirect("/list-kham")
            else:
                err_msg = "Du lieu dau vao khong hop le!"
        except:
            err_msg = "He thong dang co loi! Vui long quay lai sau!"
    return render_template("add-hoa-don.html", err_msg=err_msg)


if __name__ == '__main__':
    app.run(debug=True)
