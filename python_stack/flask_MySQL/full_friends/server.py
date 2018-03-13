from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
@app.route('/')
def index():
    query = "SELECT full_name, age, DATE_FORMAT(created_at, '%b %e') AS friend_since, YEAR(created_at) AS year FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()

    print friends


    return render_template('index.html', all_friends=friends) # pass data to our template

@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (full_name, age, created_at, updated_at) VALUES (:full_name, :age, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'full_name': request.form['full_name'],
             'age':  request.form['age'],
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
