# Ini file nya kalo mau ngikutin tutorial harus kek gini namanya
# soalnya kalo jadi __init__.py si folder nya jadi keitung python package
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'Suzy Cakep'
    db.init_app(app)

    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route("/login")
    def login():
        return render_template('login_miles.html', title='Login')

    @app.route("/regis_investor", methods=["POST", "GET"])
    def regis_investor():
        # form = Investor(request.form)
        if request.method == 'POST':  # Registrasi di websitenya blom diminta password
            email = request.form.get('email')
            forename = request.form.get('forename')
            surname = request.form.get('surname')
            company = request.form.get('company_name')
            phone = request.form.get('phone_number')
            gender = request.form.get('gender')
            category = request.form.get('category_pref')
            budget = request.form.get('budget')
            startuplocation = request.form.get('startuplocation')
            numberofpeople = request.form.get('team_amount')
            stage = request.form.get('dev_stage')
            returntype = request.form.get('return_type_invest')
            print(email)

            if len(email) < 4:
                flash('Please enter a valid email.', category='error')
            elif len(forename) < 2:
                flash('Forename must be greater than 1 character.', category='error')
            elif len(phone) < 8:
                flash('Please enter a valid phone number.', category='error')
            else:
                # bagian database samain nama classnya dgn ini "User", ini asumsi database udh selesai
                new_Investor = Investor(email=email, forename=forename, surname=surname, company=company, phone=phone,
                                    gender=gender, category=category, budget=budget, startuplocation=startuplocation,
                                    numberofpeople=numberofpeople, stage=stage, returntype=returntype)
                db.session.add(new_Investor)
                db.session.commit()
                print('telah ditambahkan')
            return redirect('/home')
        else:
            return render_template('regis_investor.html')

    @app.route("/regis_investor/preference")
    def pref_investor():
        return render_template('pref_investor.html')

    @app.route("/regis_startup", methods=["POST", "GET"])
    def regis_startup():
        if request.method == "POST":
            email = request.form.get('email')
            fullname = request.form.get('full_name')
            name = request.form.get('name')
            location = request.form.get('location')
            category = request.form.get('category')
            desc = request.form.get('description')
            budget = request.form.get('budget_need')
            phone = request.form.get('phone_number')
            gender = request.form.get('gender')
            company_location = request.form.get('company_location')
            return_type = request.form.get('return_type_startup')
            other_support = request.form.get('radio')
            support_need = request.form.get('support')
            print(email)

            if len(email) < 4:
                flash('Please enter a valid email.', category='error')
                print('error')
            elif len(fullname) < 2:
                flash('Forename must be greater than 1 character.', category='error')
                print('error')
            elif len(phone) < 8:
                flash('Please enter a valid phone number.', category='error')
                print('error')
            else:
                # bagian database samain nama classnya dgn ini "User", ini asumsi database udh selesai
                new_Startup = Startup(email=email, full_name=fullname, name=name,location=location, category=category,
                                       description=desc, phone_number=phone,
                                        gender=gender, budget_need=budget,
                                        company_location = company_location,
                                        return_type_startup=return_type, additional_support=support_need)
                db.session.add(new_Startup)
                db.session.commit()
                print(new_Startup)
            return redirect(url_for('home'))  # ini diganti apa ya gatau gua
        else:
            return render_template('regis_startup.html')
    @app.route("/startups")
    def startups():
        #  startups =
        return render_template('search_filter_startup.html', title='Startups', data=Startup.query.all())

    @app.route("/electronics")
    def electronics():
        return render_template('electronics.html', title='Electronics',
                               data=Startup.query.filter_by(category="Electronics")) # ini buat ngetest doang

    @app.route("/clothings")
    def clothings():
        return render_template('clothings.html', title='Clothings',data=Startup.query.filter_by(category="Clothings"))

    @app.route("/foodndrinks")
    def foodndrinks():
        return render_template('foodndrinks.html', title='Food and Drink',data=Startup.query.filter_by(category='Food and Drink'))

    @app.route("/games")
    def games():
        return render_template('games.html', title='Games',data=Startup.query.filter_by(category='Games'))
    @app.route("/investor")
    def investor():
        return render_template('search_filter_investor.html',title="Investors",data=Investor.query.all())

    @app.route("/fintech")
    def fintech():
        return render_template('fintech.html',data=Investor.query.filter_by(category='Fintech'))

    @app.route("/education")
    def education():
        return render_template('education.html',data=Investor.query.filter_by(category='Education'))

    @app.route("/service")
    def service():
        return render_template('service.html',data=Investor.query.filter_by(category='Service'))

    @app.route("/agriculture")
    def agriculture():
        return render_template('agriculture.html',data=Investor.query.filter_by(category='Agriculture'))

    @app.route("/technology")
    def technology():
        return render_template('technology.html',data=Investor.query.filter_by(category='Technology'))
    # bikin database
    from .models import Startup,Investor

    create_database(app)

    return app

def create_database(app):
    if not path.exists('/Website/database.db'):
        db.create_all(app=app)
        print("Database berhasil dibuat")