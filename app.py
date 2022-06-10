from flask import Flask, request, render_template, url_for, redirect, session
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="template")

app.secret_key = "Gajexa"
app.permanent_session_lifetime = timedelta(seconds=40)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RegisterDatabase.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class RegisterDatabase (db.Model) :
    id = db.Column('user_id', db.Integer, primary_key=True)
    userName = db.Column(db.String(30))
    email = db.Column(db.String(40))
    password = db.Column(db.String(30))

db.create_all()

@app.route('/registration', methods=['POST', 'GET'])
def registraion():
    if request.method == 'POST':
        userName = request.form["nameUser"]
        email = request.form ["emailUser"]
        password = request.form ["passwordUser"]
        user_info = RegisterDatabase (userName = userName, email = email, password = password)
        db.session.add(user_info)
        db.session.commit()

        return redirect(url_for('login'))
    else:
        return render_template('registration.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login',  methods=['POST', 'GET'])
def login_validation():
    if request.method == 'POST':
        email = request.form["emailUser"]
        password = request.form["passwordUser"]
        user = RegisterDatabase.query.filter_by(email=email,password = password).first()
        session["client"] = email
        try:
            if user.password == password and user.email == email:
                return redirect(url_for("mainPage"))
        except:
            return render_template("login.html")

    else:
        if "client" in session:
            return redirect(url_for('mainPage'))



@app.route("/main_page")
def mainPage():
    if "client" in session:
        return render_template('mainPage.html')
    else:
        return redirect(url_for("login"))
