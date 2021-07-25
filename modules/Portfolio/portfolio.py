from flask import Blueprint, render_template, redirect, session, flash

portfolio = Blueprint(
    "portfolio",
    __name__, 
    template_folder="templates"
)

@portfolio.route("/")
def my_portfolio():
    if "email" in session:
        email = session["email"]
        return render_template("portfolio.html", email=email)
    else:
        return render_template("signin.html", status="401")