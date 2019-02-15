import requests, json
from flask import Flask, render_template, redirect, request, jsonify
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy import create_engine
import queries
import yaml

config = yaml.load(open('../config.yaml'))

engine = create_engine(config['postgresql'])
conn = engine.connect()


app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = config['google_api']

app.config['SQLALCHEMY_DATABASE_URI'] = config['postgresql']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True

app.debug = True
db = SQLAlchemy(app)

class Results(db.Model):
    __tablename__ = 'result'

    name = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def serialize(self):
        return {
            'name': self.name, 
            'address': self.address,
            'latitude': self.latitude,
            'longitude':self.longitude
        }

class Input(db.Model):
    """Model for the stations table"""
    __tablename__ = 'input'

    id = db.Column(db.Integer, primary_key=True)
    user1 = db.Column(db.Integer)
    user2 = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

db.create_all()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/restaurant")
def restaurant():
    if request.method == 'POST':
        user1 = request.form.get['user1']
        user2 = request.form.get['user2']
        la = request.form.get['la']
        lo = request.form.get['lo']
        return redirect(url_for('mapview'), user1 = user1, user2 = user2, lat=la, lng=lo)
    else:
        return render_template('restaurant.html')

# GoogleMaps(app)

@app.route('/mapview', methods=['POST'])
def mapview():

    user1 = request.form['user1']
    user2 = request.form['user2']
   
    la = request.form['la']
    lo = request.form['lo']
    

    Queries.get_result(int(user1), int(user2), float(la), float(lo))

    query = Results.query.all()
    data = []
    for item in query:
        i = {
            'name':item.name,
            'address':item.address,
            'latitude':item.latitude,
            'longitude':item.longitude
            }
        data.append(i)
   
    return render_template('mapview.html',  data = data, user1=user1, user2=user2, la=la, lo=lo)


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=80
    )