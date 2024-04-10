from flask import Blueprint, render_template
from admin.templates import "home.html"

second = Blueprint("second", __name__, static_folder="static", template_folder="templates")

@second.route("/home")
@second.route("/")
def home():
    return render_template("home.html")

@second.route("/test")
def test():
    return render_template("<p>test</p>")