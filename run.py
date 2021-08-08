from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    #sementara navabr dlu ya gaess sampe homenya jadi
    return render_template('navbar.html') 

@app.route("/login")
def login():
    return render_template('login_miles.html', title='Login')

@app.route("/regis_investor")
def regis_investor():
    return render_template('regis_investor.html')

@app.route("/pref_investor")
def pref_investor():
    return render_template('pref_investor.html')

if __name__ == '__main__':
    app.run(debug=True)