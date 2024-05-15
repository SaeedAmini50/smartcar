from flask import Blueprint

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