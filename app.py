from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "eevee"

@app.route("/hello")
def index():
	flash("What's your name?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hello " + str(request.form['name_input']) + ", buenaventura")
	return render_template("index.html")