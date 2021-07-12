from flask import Blueprint, render_template

crypto = Blueprint(
    "crypto",
    __name__, 
    template_folder="templates"
)

@crypto.route("/")
def crypto_list():
    return render_template("crypto.html")