# views.py
from flask import Blueprint, render_template
from .models import get_products

views = Blueprint('views', __name__)

@views.route('/')
def index():
    products = get_products()
    return render_template("index.html", products=products)
