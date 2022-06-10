from flask import Flask, request, render_template, url_for, redirect, session
app = Flask(__name__, template_folder="template")
from datetime import datetime, timedelta
# from flask_sqlalchemy import SQLAlchemy


app.secret_key = "Gajexa"
app.permanent_session_lifetime = timedelta(seconds=10)

# class model :
#     id = db.Column('user_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(30))
#     email = db.Column(db.String(40))
#     password = db.Column(db.String(30))

@app.route('/registration', methods=['POST', 'GET'])
def registraion():
    if request.method == 'POST':
        # user = request.form["nameUser"]
        # request.form ["emailUser"]
        # request.form ["passwordUser"]
        # user_info = model (name = name, email = email, password = password)
        # db.session.add(user_info)
        # db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('registration.html')


@app.route('/login',  methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form["emailUser"]
        password = request.form["passwordUser"]
        session["client"] = email, password
        return redirect(url_for("mainPage"))
    else:
        if "client" in session:
            return redirect(url_for('mainPage'))

    return render_template("login.html")



@app.route("/main_page")
def mainPage():


    return render_template('mainPage.html')
