import os
import pyrebase
from dotenv import load_dotenv
from flask import Blueprint, render_template, request
import requests

crypto = Blueprint(
    "crypto",
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
    print(" * Database Connected with Coins")
except:
    print(" * Failed to connect with Database")

@crypto.route("/")
def coins_list():
    return render_template("coins_list.html")

@crypto.route("/coin")
def coin():
    coin_id = request.args.get('id')
    URL = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin_id}&per_page=1&page=1&sparkline=false"
    r = requests.get(url = URL)
    return render_template("coin.html", coin=r.json(), coin_id=coin_id)
