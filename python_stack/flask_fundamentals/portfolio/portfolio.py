from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', endpoint="index")
@app.route('/projects', endpoint="projects")
@app.route('/about', endpoint="about")
def portfolio():
    if request.endpoint == "index":
        return render_template("index.html")
    elif request.endpoint == "projects":
        return render_template("projects.html")
    elif request.endpoint == ("about"):
        return render_template("about.html")
app.run(debug=True)