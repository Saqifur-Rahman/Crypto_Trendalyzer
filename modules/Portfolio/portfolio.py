from flask import Blueprint, render_template

portfolio = Blueprint(
    "portfolio",
    __name__, 
    template_folder="templates"
)

@portfolio.route("/")
def my_portfolio():
    return render_template("portfolio.html")