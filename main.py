from flask import Flask, render_template      
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import psycopg2
from config import config

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db' #Setup a postgres to just start with anyways. Setup a database.ini file.
db = SQLAlchemy(app)

""" class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    posts = db.relationship('Post', backref = 'author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False),
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.username}', '{self.date_posted}')" """

    #The above information is old and can likely be deleted.

def connect():
    conn = None
    try:
        params = config()

        print("Connecting to the database server...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        print("Database Version:")
        cur.execute('SELECT Version();')
        
        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/test")
def test():
    return "Hello, this is a test"

@app.route("/profile")
def about():
    return render_template("profile.html")

@app.route("/template")
def template():
    return render_template("template.html")
    
if __name__ == "__main__":
    app.run(debug=True)
    connect()
