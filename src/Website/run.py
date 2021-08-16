from flask import Flask, render_template, url_for, request, redirect ,flash
from . import db
from .models import Startup,Investor
app = Flask(__name__)


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

@app.route("/regis_startup/preference")
def pref_startup():
    return render_template('pref_startup.html')
@app.route("/startups")
def startups():
  #  startups = 
    return render_template('search_filter_startup.html', title='Startups',startup_data = startups)

@app.route("/electronics")
def electronics():
    return render_template('electronics.html', title='Electronics')

@app.route("/clothings")
def clothings():
    return render_template('clothings.html', title='Clothings')

@app.route("/foodndrinks")
def foodndrinks():
    return render_template('foodndrinks.html', title='Food and Drink')

@app.route("/games")
def games():
    return render_template('games.html', title='Games')

@app.route("/investor")
def investor():
    return render_template('search_filter_investor.html',title="Investors",data=Investor.query.all())

@app.route("/fintech")
def fintech():
    return render_template('fintech.html')

@app.route("/education")
def education():
    return render_template('education.html')

@app.route("/service")
def service():
    return render_template('service.html')

@app.route("/agriculture")
def agriculture():
    return render_template('agriculture.html')

@app.route("/technology")
def technology():
    return render_template('technology.html')

if __name__ == '__main__':
    app.run(debug=True)