from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/ninjas')
def ninjas():
    return render_template("ninja.html")

@app.route('/ninjas/<ninja_color>')
def ninjatype(ninja_color):

    if ninja_color=="blue" or ninja_color=="red" or ninja_color=="purple" or ninja_color=="orange":

        temp = "ninja_"+ninja_color+".html"
       
    else:
        
        temp = "ninja_nope.html"

    return render_template(temp)

app.run(debug=True)