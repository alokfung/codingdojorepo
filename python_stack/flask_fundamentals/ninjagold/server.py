from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "weiohfweoufiowef"

import random, datetime, time

@app.route('/')
def index():
    if session.get("gold") is None:
        session["gold"]=0
        session["activity"] = ""
    
    print session["gold"]
    print session["activity"]
    return render_template("index.html", gold=session["gold"], act=session["activity"])

@app.route('/process_money', methods=['POST'])
def process_money():
    # Timestamp from Python
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    if request.form['building'] == 'farm':
        temp=random.randrange(10,21)
        session["gold"]+=temp
        session["activity"] = session["activity"] + "Earned " + str(temp) + " from the " + request.form['building'] + "! " + st + "\n"
    elif request.form['building'] == 'cave':
        temp=random.randrange(5,11)
        session["gold"]+=temp
        session["activity"] = session["activity"] + "Earned " + str(temp) + " from the " + request.form['building'] + "! " + st + "\n"
    elif request.form['building'] == 'house':
        temp=random.randrange(2,6)
        session["gold"]+=temp
        session["activity"] = session["activity"] + "Earned " + str(temp) + " from the " + request.form['building'] + "! " + st + "\n"       
    elif request.form['building'] == 'casino':
        temp=random.randrange(-50,50)
        session["gold"]+=temp
        session["activity"] = session["activity"] + "Earned/lost " + str(temp) + " from the " + request.form['building'] + "! ...ouch..." + st + "\n"
        if session["gold"]<0:
            session["gold"]=0
            session["activity"] += "You are bankrupt! HAH!\n"
    return redirect('/')


app.run(debug=True)