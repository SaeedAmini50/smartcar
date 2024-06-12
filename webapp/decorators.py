from functools import wraps
from flask import session, redirect, url_for, flash
from webapp.mydb import get_db
import mysql.connector

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            flash('You need to be signed in to view this page.', 'danger')
            return redirect(url_for('auth.signin'))
        
        email = session['email']
        
        try:
            cnx = get_db()
            cursor = cnx.cursor()
            query = "SELECT * FROM admin WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()
            cnx.close()
            
            if result is None or result[0] != 'admin':
                flash('You do not have the required permissions to view this page.', 'danger')
                return redirect(url_for('views.index'))
        except mysql.connector.Error as err:
            print(err)
            flash('An error occurred. Please try again later.', 'danger')
            return redirect(url_for('views.index'))

        return f(*args, **kwargs)
    return decorated_function
