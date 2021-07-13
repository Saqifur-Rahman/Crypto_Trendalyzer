from flask import Flask, render_template
import requests
from modules.Crypto.crypto import crypto
from modules.Portfolio.portfolio import portfolio

app = Flask(__name__)
app.secret_key = "crypto_trendalyzer"

# Blueprints
app.register_blueprint(crypto, url_prefix="/crypto")
app.register_blueprint(portfolio, url_prefix="/portfolio")

@app.route("/")
def home():
    # Events
    URL = "https://api.coingecko.com/api/v3/events"
    events = requests.get(url = URL).json()

    API_KEY = "6291b4b15cbb429bba5f669b7d773b00"
    URL2 = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_KEY}&pageSize=9"
    news = requests.get(url = URL2).json()
    
    return render_template("home.html", events=events, news=news)

if __name__ == "__main__":
    app.run(debug=True)