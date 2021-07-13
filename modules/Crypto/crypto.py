from flask import Blueprint, render_template, request
import requests

crypto = Blueprint(
    "crypto",
    __name__, 
    template_folder="templates"
)

@crypto.route("/")
def coins_list():
    return render_template("coins_list.html")

@crypto.route("/coin")
def coin():
    coin_id = request.args.get('id')
    URL = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin_id}&per_page=1&page=1&sparkline=false"
    r = requests.get(url = URL)
    return render_template("coin.html", coin=r.json())
