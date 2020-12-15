from functools import wraps
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from authlib.integrations.flask_client import OAuth
import os
from datetime import timedelta
from flask_web_log import Log

app = Flask(__name__)
mysql = MySQL(app)
Log(app)
oauth = OAuth(app)

app.secret_key = ''
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
app.config['TESTING'] = False

google = oauth.register(
    name='google',
    client_id="",
    client_secret="",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
)

app.config["LOG_TYPE"] = "CSV"
app.config["LOG_FILENAME"] = "logging"
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

@app.route('/')
def root():  
    return render_template('index.html')

@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    user = oauth.google.userinfo() 
    session['email'] = user_info['email']
    session['name'] = user_info['name']
    session.permanent = True
    session['logged_in'] = True
    return redirect(url_for('home'))

@app.route('/home')
def home():
    if session.get('logged_in'):
        session['email'] = dict(session).get('email')
        session['name'] = dict(session).get('name')
        return render_template('home.html', name=session['name'], email=session['email'])
    else:
        return redirect(url_for('root'))
    
@app.route('/profile')
def profile():
    if session.get('logged_in'):
        session['email'] = dict(session).get('email')
        session['name'] = dict(session).get('name')
        return render_template('profile.html', name=session['name'], email=session['email'])
    else:
        return redirect(url_for('root'))

@app.route('/products', methods=['GET', 'PUT'])
def product_page():
    if session.get('logged_in'):
        if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_detail")
            data = cur.fetchall()
            cur.close()
            return render_template('products.html', products = data)
        elif request.method == 'PUT':
            id = request.form['id']
            name = request.form['name']
            stock = request.form['stock']
            price = request.form['price']
            supplier = request.form['supplier']
            description = request.form['description']
            cur = mysql.connection.cursor()
            cur.execute("UPDATE product_detail SET name = %s, stock = %s, price = %s, supplier = %s, description = %s WHERE id = %s", [
                        name, stock, price, supplier, description, id, ])
            mysql.connection.commit()
            return jsonify({'message': 'Product ' + name + ' successfully updated!'})
    else:
        return redirect(url_for('root'))

@app.route('/product/<string:id>/details', methods=['GET', 'PUT', 'DELETE'])
def get_products_details(id):
    if session.get('logged_in'):
        if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute(
                "SELECT * FROM product_detail WHERE id = %s", [id, ])
            data = cur.fetchall()
            cur.close()
            return render_template('product_details.html', products = data)   
        elif request.method == 'PUT':
            id_details = request.form['id']
            name_details = request.form['name']
            stock_details = request.form['stock']
            price_details = request.form['price']
            supplier_details = request.form['supplier']
            description_details = request.form['description']
            cur = mysql.connection.cursor()
            cur.execute("UPDATE product_detail SET name = %s, stock = %s, price = %s, supplier = %s, description = %s WHERE id = %s", [
                        name_details, stock_details, price_details, supplier_details, description_details, id_details, ])
            mysql.connection.commit()
            return jsonify({'message': 'Product ' + name_details + ' successfully updated!'})
    else:
        return redirect(url_for('root'))

@app.route('/insert', methods=['POST'])
def insert():
    if session.get('logged_in'):
        name_new = request.form['name']
        stock_new = request.form['stock']
        price_new = request.form['price']
        supplier_new = request.form['supplier']
        description_new = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO product_detail (name, stock, price, supplier, description) VALUES (%s, %s, %s, %s, %s)", (name_new, stock_new, price_new, supplier_new, description_new))
        mysql.connection.commit()
        return jsonify({'message': 'Product ' + name_new + ' successfully added!'})
    else:
        return redirect(url_for('root'))

@app.route('/product/<string:id>', methods=['GET'])
def get_products_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product_detail WHERE id = %s", [id,])
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/product-list', methods=['GET'])
def get_products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product_detail")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/delete/<string:id>', methods=['GET'])
def delete_by_id(id):
    if session.get('logged_in'):
        cur1 = mysql.connection.cursor()
        cur1.execute("SELECT name from product_detail WHERE id = %s", [id, ])
        cur1res = cur1.fetchone()
        name = cur1res[0]
        mysql.connection.commit()

        cur2 = mysql.connection.cursor()
        cur2.execute("DELETE FROM product_detail WHERE id = %s", [id,])
        mysql.connection.commit()
        return redirect(url_for('product_page'))
    else:
        return redirect(url_for('root'))

@app.route('/delete', methods=['DELETE'])
def delete():
    if session.get('logged_in'):
        iddel = request.form['id']
        cur1 = mysql.connection.cursor()
        cur1.execute("SELECT name from product_detail WHERE id = %s", [iddel, ])
        cur1res = cur1.fetchone()
        name = cur1res[0]
        mysql.connection.commit()

        cur2 = mysql.connection.cursor()
        cur2.execute("DELETE FROM product_detail WHERE id = %s", [iddel, ])
        mysql.connection.commit()
        return jsonify({'message': 'Product ' + name + ' successfully deleted!'})
    else:
        return redirect(url_for('root'))

@app.route('/update/<string:id>', methods=['POST'])
def update(id):
    if session.get('logged_in'):
        id = request.form['id']
        name = request.form['name']
        stock = request.form['stock']
        price = request.form['price']
        supplier = request.form['supplier']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product_detail SET name = %s, stock = %s, price = %s, supplier = %s, description = %s WHERE id = %s", [name, stock, price, supplier, description, id,])
        mysql.connection.commit()
        return redirect(url_for('product_page'))
    else:
        return redirect(url_for('root'))

@app.route('/logout')
def logout():
    if session.get('logged_in'):
        for key in list(session.keys()):
            session.pop(key)
        return redirect(url_for('root'))

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000,host='0.0.0.0')

