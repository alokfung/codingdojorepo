from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)

app.secret_key = "weiofnwegkjfwe"

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/result', methods=["POST"])
def result():
    if len(request.form["full_name"]) < 1 or len(request.form["comment"]) < 1:
        flash("Name and comments cannot be empty!")
        return redirect("/")
    else:
        flash("Success! Your name is {}".format(request.form['full_name']))
    
    if len(request.form["comment"]) > 120:
        flash("Comment is too long! Cannot exceed 120 characters.")
        return redirect("/")


    return render_template("result.html", full_name = request.form["full_name"], dlocation = request.form["dlocation"], language =  request.form["language"], comment = request.form["comment"])
app.run(debug=True)