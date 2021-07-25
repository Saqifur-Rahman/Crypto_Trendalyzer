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