from flask import Flask, render_template, url_for, flash, redirect, session, request, logging
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from . import db
from .models import Startup,Investor

# disini ada bagian database tp saya gak ngerti @@
db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html') 

@app.route("/login", methods['GET', 'POST'])
def login():
    #if request.method == 'POST': # Bagian sini masi rada bingung, blm ngerti cara nge refer ke databasenya + blom ada password juga di registrasinya
        #data = request.form
        #email = data.get('email')
        #password = data.get('password')
        
        #user = User.query.filter_by(email=email).first()
        #if user:
        #    if check_password_
        
    return render_template('login_miles.html', title='Login')



@app.route("/regis_investor", methods=['GET', 'POST'])
def regis_investor():
    form = Investor(request.form)
    if request.method == 'POST': # Registrasi di websitenya blom diminta password
        email = request.form.get('email')
        forename = request.form.get('forename')
        surname = request.form.get('surname')
        company = request.form.get('company')
        phone = request.form.get('phone')
        gender = request.form.get('gender')
        category = request.form.get('category')
        budget = request.form.get('budget')
        startuplocation = request.form.get('startuplocation')
        numberofpeople = request.form.get('numberofpeople')
        stage = request.form.get('stage')
        returntype = request.form.get('returntype')
        
        if len(email) < 4:
            flash('Please enter a valid email.', category='error')
        elif forename < 2:
            flash('Forename must be greater than 1 character.', category='error')
        elif phone < 8:
            flash('Please enter a valid phone number.', category='error')
        else:
            # bagian database samain nama classnya dgn ini "User", ini asumsi database udh selesai
            new_user = User(email=email, forename=forename, surname=surname, company=company, phone=phone, gender=gender, category=category, budget=budget, startuplocation=startuplocation, numberofpeople=numberofpeople, stage=stage, returntype=returntype)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect('/home')
            

        return redirect(url_for('index'))
    return render_template('regis_investor.html', form=form)

@app.route("/regis_investor/preference")
def pref():
    return render_template('pref_investor.html')

if __name__ == '__main__':
    app.run(debug=True)