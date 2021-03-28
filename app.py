from flask import Flask, render_template, url_for, request, session, redirect

from flask_pymongo import PyMongo
import bcrypt

from pymongo import MongoClient


app = Flask(__name__,template_folder='template')

app.config['MONGO_DBNAME'] = 'mongologinexample'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mongologinexample'

mongo = PyMongo(app)

@app.route('/index')
def index():
    
    return render_template('index.html')

'''@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/register')
def regiter():
    return render_template('register.html')

@app.route('/Page')
def Page():
    
    return render_template('Page.html')


@app.route('/Success')
def Success():
    
    return render_template('Success.html')

@app.route("/")
def home():
    return "Hello, User!"


if __name__ == "__main__":
    app.run(debug=True)    
'''
if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
    '''