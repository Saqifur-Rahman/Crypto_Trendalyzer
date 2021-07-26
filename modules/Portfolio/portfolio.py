import pyrebase
import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, redirect, session

portfolio = Blueprint(
    "portfolio",
    __name__, 
    template_folder="templates"
)

load_dotenv()

config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "databaseURL" : os.getenv("FIREBASE_DATABASE_URL"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID")
}

try:
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    print(" * Database Connected with Portfolio")
except:
    print(" * Failed to connect with Database")

@portfolio.route("/")
def my_portfolio():
    if "email" in session:
        email = session["email"]
        return render_template("portfolio.html", email=email)
    else:
        return render_template("signin.html", status="401")

def getCoinValue(portfolio_id, coin):
    found=False
    # check if portfolio exists
    for pf in db.child("portfolios").get():
        if pf.key() == portfolio_id:
            found=True
            break
    if not found:
        return 0
    # if exists 
    portfolios = db.child("portfolios").child(portfolio_id).get()
    for pf in portfolios:
        if pf.key() == coin:
            return pf.val()
    return 0

@portfolio.route("/test")
def test():
    curr_val = getCoinValue("xyz", "cardano")
    # db.child("portfolios").child("xyz").update({"bitcoin": 100})
    return f"<h1>{curr_val}</h1>"