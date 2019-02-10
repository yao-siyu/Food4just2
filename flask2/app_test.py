import requests, json
from flask import Flask, render_template, redirect, request, jsonify
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask import url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test_user:insight@34.222.230.25:5432/test'
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
        #return '<Rsults %r>' % self.name, self.address, self.latitude, self.longitude
        return '<name {}>'.format(self.name)

    def serialize(self):
        return {
            'name': self.name, 
            'address': self.address,
            'latitude': self.latitude,
            'longitude':self.longitude
        }

# GoogleMaps(app)

@app.route("/")

def mapview():
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
    #result = json.dumps(data)
    return render_template('map.html',  data = data)
    #name = [result.name for result in results]
    #address = [result.address for result in results]
    #latitude = [result.latitude for result in results]
    #longitude = [result.longitude for result in results]
    
    #return render_template('map.html', name = name, address = address, latitude = latitude, longitude = longitude)    

    """
    #result = json.dumps(jsonify([i.serialize() for i in query]))
    #user1 = request.form['user1']
    #user2 = request.form['user2']
    return render_template('test.html',  result = result)
    #return render_template('test.html', name = name, address = address, latitude = latitude, longitude = longitude)


@app.route('/model', methods=['GET','POST'])
def getResult():
    user1 = request.form.get('user1')
    user2 = request.form.get('user2')
    print (user1)
    print (user2)

    sw_latitude = request.form.get('sw_latitude')
    sw_longitude = request.form.get('sw_longitude')
    ne_latitude = request.form.get('ne_latitude')
    ne_longitude = request.form.get('ne_longitude')
    checkbox1 = request.form.get('checkbox1')
    bounding_box = {
        'sw_latitude': sw_latitude,
        'sw_longitude': sw_longitude,
        'ne_latitude': ne_latitude,
        'ne_longitude': ne_longitude
    }
    user_id = {
        "user1": user1,
        "user2": user2,
    }
    search_param = {

    }
    # result = supervisor(user_id,bounding_box,search_param)
    return str(checkbox1)
"""



if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=80
    )