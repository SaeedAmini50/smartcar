# views.py
from flask import Blueprint, render_template, request
from .models import get_products_ending_with_a, get_product_by_id

views = Blueprint('views', __name__)

@views.route('/')
def index():
    products = get_products_ending_with_a()
    return render_template("index.html", products=products)

@views.route('/product/<int:product_id>')
def show_product(product_id):
    product = get_product_by_id(product_id)
    return render_template("show_product.html",product=product)