import os.path
import requests
import json
from flask import Flask, request, render_template, redirect, url_for, jsonify
application = Flask(__name__)


class Class(object):
    def __init__(self, name, buildingNumber):
        self.name = name
        self.buildingNumber = buildingNumber


def strip_data(data):
    finalDict = dict()
    for i in data:
        element = data[i][0]
        bNum = element["metadata"]["buildingNum"]
        if bNum is None or element["campusID"] != 0:
            continue
        else:
            finalDict[bNum] = {
                    "title": element["title"],
                    "latitude": element["latitude"],
                    "longitude": element["longitude"]
            }
    return finalDict


def fetch_data():
    if not os.path.isfile("location.cache"):
        locationFile = open("location.cache", "w")
        r = requests.get("http://uqmaps.app.uq.edu.au/json/locations")
        data = strip_data(r.json())
        locationFile.write(json.dumps(data))
        locationFile.close()

    # Read from file now
    locationFile = open("location.cache", "r")
    data = json.loads(locationFile.read())
    locationFile.close()
    return data

@application.route('/get_locations')
def get_locations():
    data = fetch_data()
    return jsonify(result=data)


@application.route('/')
def gps_route():
    return render_template('findroute.html')

if __name__ == "__main__":
    application.run(debug=False, host='0.0.0.0')
