from flask import Flask, render_template, url_for, flash, redirect, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html') 

@app.route("/login")
def login():
    return render_template('login_miles.html', title='Login')

class InvestorRegister(Form):
    email = StringField('Email')
    forename = StringField('Forename')
    surname = StringField('Surname')
    company = StringField('Company/Organization')
    phone = StringField('Phone Number')
    gender = StringField('Gender')
    category = StringField('Category Preference')
    budget = StringField('Investing Budget')
    startuplocation = StringField('Location of Startup')
    numberofpeople = StringField('Number of People in the Team')
    stage = StringField('Development Stage')
    returntype = StringField('Return Type')    

@app.route("/regis_investor", methods=['GET', 'POST'])
def regis_investor():
    form = InvestorRegister(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = MySQL.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        MySQL.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('index'))
    return render_template('regis_investor.html', form=form)

@app.route("/regis_investor/preference")
def pref():
    return render_template('pref_investor.html')

if __name__ == '__main__':
    app.run(debug=True)