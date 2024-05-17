from flask import Blueprint,render_template

auth= Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('sing_up')
def sing_up():
    return "<h1>sing up<h1>"

@auth.route('/show_product')
def show_product():
    return render_template("show_product.html")  