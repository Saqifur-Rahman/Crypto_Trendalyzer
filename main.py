from flask import Flask, render_template
from modules.Crypto.crypto import crypto
from modules.Portfolio.portfolio import portfolio

app = Flask(__name__)
app.secret_key = "crypto_trendalyzer"

# Blueprints
app.register_blueprint(crypto, url_prefix="/crypto")
app.register_blueprint(portfolio, url_prefix="/portfolio")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)