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

    
if __name__ == '__main__':
    app.run(debug=True)