from flask import Flask, render_template, url_for, request, redirect 
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html') 

@app.route("/login")
def login():
    return render_template('login_miles.html', title='Login')

@app.route("/regis_investor", methods = ["POST","GET"])
def regis_investor():
    if request.method == "POST":
        # disini bisa input ke data base
        # misal mau ngambil data caranya:
        investor_data = request.form
        # bisa diliat datanya ke post di terminal
        print(investor_data)
        return redirect(url_for("startups"))
    else:
        return render_template('regis_investor.html')

@app.route("/regis_investor/preference")
def pref_investor():
    return render_template('pref_investor.html')

@app.route("/regis_startup", methods=["POST","GET"])
def regis_startup():
    if request.method == "POST":
        startup_data = request.form
        print(startup_data)
        return redirect(url_for('home')) # ini diganti apa ya gatau gua
    else:
        return render_template('regis_startup.html')

@app.route("/regis_startup/preference")
def pref_startup():
    return render_template('pref_startup.html')

@app.route("/startups")
def startups():
  #  startups = 
    return render_template('search_filter.html', title='Startups',startup_data = startups)

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

if __name__ == '__main__':
    app.run(debug=True)