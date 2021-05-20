from flask import Flask
from __main__ import app
from Models.user import User

@app.route('/user/signup', methods=["POST"])
def usersignup():
    return User().signup()

@app.route('/user/login', methods=["POST"])
def userlogin():
    return User().login()

@app.route('/user/signout')
def usersignout():
    return User().signout()
