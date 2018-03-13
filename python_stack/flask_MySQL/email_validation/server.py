from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)   
app.secret_key = 'wegwehwehwehweh'
mysql = MySQLConnector(app,'email_validation')
@app.route('/')
def index():
    if session.get('cc') is None:
        session['cc']=""

    return render_template('index.html', cc=session['cc'])

@app.route('/success', methods=['POST'])
def create():

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        session['cc'] = "red"
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        session['cc'] = "red"
        return redirect('/')
    else:
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
                'email': request.form['email']
            }
        mysql.query_db(query, data) #This runs the query defined in query and data above
        flash("The email address "+request.form['email']+" is a VALID email address! Thank you!" )
        session['cc'] = "green"

        query = "SELECT email, created_at FROM users" #new query
        email = mysql.query_db(query)  #run the select query to retrieve the users table
        
        return render_template('success.html', email=email, cc=session['cc'])
        
app.run(debug=True)
