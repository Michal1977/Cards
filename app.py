from flask import  Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)


@app.route("/visitcard")
def card():
    return render_template("visiting_card_contact.html")


@app.route("/form")
def form():
    return render_template("visiting_card_form.html")