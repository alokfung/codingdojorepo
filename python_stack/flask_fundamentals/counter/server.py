from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def homepage():
    if "count" in session:
        session["count"]+=1
    else:
        session["count"]=1

    print session

    return render_template("index.html")
app.run(debug=True)