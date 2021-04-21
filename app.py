from flask import Flask, request, render_template, url_for
import ipapi
import requests
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/ip_db"

mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def iptracker():
    search = request.form.get('search')
    data = ipapi.location(ip=search, output='json')

    ip = data.get('ip')
    city = data.get('city')
    country = data.get('country')
    languages = data.get('languages')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    timezone = data.get('timezone')
    country_calling_code = data.get('country_calling_code')
    currency = data.get('currency')
    org = data.get('org')
    postal = data.get('postal')

    mongo.db.ip_data.insert_one({'ip': ip, 'city': city, 'country': country, 'languages': languages, 'latitude': latitude, 'longitude': longitude, 'timezone': timezone, 'country_calling_code': country_calling_code, 'currency': currency, 'org': org, 'postal': postal})

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
