from flask import Blueprint, request, render_template, redirect, url_for

bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")
