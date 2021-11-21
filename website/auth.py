#File that stores the routes for the website

#import
from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from .models import User
from flask import redirect, url_for
from . import db
from flask_login import login_user, login_required, logout_user, current_user

#clases
auth = Blueprint('auth', __name__)

#routes
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')

        #quering the database to validate entry from user
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Logged In Successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password/Email. Please try again', category='error')
        else:
            flash('Email does not exists', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        #get info from form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #validation
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email Already Exists', category='error')
        elif len(email) < 4:
            flash('E-Mail Account must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password too short. Password must be at least 7 characters', category='error')
        else:
            #add user to database
            new_user = User(email=email, first_name=first_name, password=password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account Created Successfully', category='success')
            #redirect to the home.html
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

