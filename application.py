import os.path
import requests
import json
from flask import Flask, request, render_template
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


def request_location_info(nodes):
    data = fetch_data()
    nodePath = []
    for i in nodes:
        bnName = data[i.buildingNumber]["title"]
        nLat = data[i.buildingNumber]["latitude"]
        nLong = data[i.buildingNumber]["longitude"]
        nodePath.append({
            "title": bnName,
            "lat": nLat,
            "lng": nLong
        })

    return nodePath


def display_map():
    classNums = request.form.getlist('buildingNumber[]')
    classNames = request.form.getlist('class[]')
    classes = []
    for i in range(0, len(classNums)):
        if classNums[i] == '' or classNames[i] == '':
            continue
        classes.append(Class(classNames[i], classNums[i]))
    nodes = request_location_info(classes)
    if len(nodes) == 0:
        return render_template('failure.html')
    return render_template('map.html', nodes=nodes)


def get_path_info():
    numList = []
    for i in fetch_data():
        numList.append(i)
    return render_template('index.html', bList=numList)


@application.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return get_path_info()
    elif request.method == 'POST':
        return display_map()
    else:
        return "This shouldn't happen"

if __name__ == "__main__":
    application.run(debug=False)
