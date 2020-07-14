from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index8.html")
@app.route("/hello",methods=["post"])
def hello():
    name = request.form.get("name")
    return render_template("hello8.html",name=name)
