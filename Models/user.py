from flask import Flask, jsonify, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256
from __main__ import db
import uuid

class User:

    def start_session(self, user):
        del user["password"]
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200


    def signup(self):

        print(request.form)

        user = {
            "_id" : uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
            "country": request.form.get('country'),
            "city": request.form.get('city'),
        }

        user["password"] = pbkdf2_sha256.encrypt(user['password'])

        if db.users.find_one({"email": user["email"]}):
            return jsonify({"error": "Ese email ya esta registrado"}), 400
        
        if db.users.insert_one(user):
            return self.start_session(user)
            

        return jsonify({"error": "El registro fallo, por favor intenta mas tarde"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        
        user = db.users.find_one({
            "email": request.form.get('email') })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)

        return jsonify({ "error": "Invalid login credentials" }), 401
       