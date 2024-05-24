from flask import Blueprint, render_template, request, redirect, url_for, session
from webapp.mydb import get_db
import hashlib
from datetime import datetime
import mysql.connector
auth= Blueprint('auth', __name__)

@auth.route('/show_product')
def show_product():
    return render_template("show_product.html")  

@auth.route('/indexAdmin.html')
def indexAdmin():
    return render_template("indexAdmin.html")  



auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        customer_name = request.form['customer_name_and_last_name']
        customer_number = request.form['customer_number']
        customer_email = request.form['email']
        customer_password = request.form['password']
        customer_password2 = request.form['customer_password2']

        if customer_password != customer_password2:
            return redirect(url_for('auth.signup', msg='invalidPassword'))

        try:
            cnx = get_db()
            cursor = cnx.cursor()

            passwordHash = hashlib.sha256(customer_password.encode()).hexdigest()

            insert_query = """
            INSERT INTO customer (customer_name_and_last_name,customer_number , email, password, customer_date)
            VALUES (%s, %s, %s, %s, %s)
            """
            data = (customer_name, customer_number, customer_email, passwordHash, datetime.now())
            cursor.execute(insert_query, data)
            cnx.commit()

            cursor.close()
            cnx.close()

            session['email'] = customer_email
            return redirect(url_for('views.index'))
        except mysql.connector.Error as err:
            print(err)
            return redirect(url_for('auth.signup', msg='error'))
    
    return render_template('signup.html')

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        customer_email = request.form['email']
        customer_password = request.form['password']

        try:
            cnx = get_db()
            cursor = cnx.cursor()

            passwordHash = hashlib.sha256(customer_password.encode()).hexdigest()

            query = """
            SELECT * FROM customer WHERE email=%s AND password=%s
            """
            cursor.execute(query, (customer_email, passwordHash))
            result = cursor.fetchone()

            if result:
                session['email'] = customer_email
                return redirect(url_for('views.index'))
            else:
                return redirect(url_for('auth.signin', msg='invalid'))
        except mysql.connector.Error as err:
            print(err)
            return redirect(url_for('auth.signin', msg='error'))

    return render_template('signin.html')