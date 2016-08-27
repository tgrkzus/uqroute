import os.path, requests, json, sys
from flask import Flask, request, redirect, jsonify, render_template
app = Flask(__name__)

class Class(object):
    def __init__(self, name, buildingNumber):
        self.name = name
        self.buildingNumber = buildingNumber

def strip_data(data):
    finalDict = dict()
    for i in data:
        element = data[i][0]
        bNum = element["metadata"]["buildingNum"]
        if bNum == None or element["campusID"] != 0:
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
    #print(locationFile.read(), file=sys.stderr)
    data = json.loads(locationFile.read())
    locationFile.close()
    return data
    
def request_location_info(nodes):
    data = fetch_data()
    nodePath = []
    for i in nodes:
        nName = data[i.buildingNumber]["title"]
        nLat = data[i.buildingNumber]["latitude"]
        nLong = data[i.buildingNumber]["longitude"]
        nodePath.append({
        "lat": nLat,
        "lng": nLong
        })

    return nodePath

def display_map():
    classes = []
    classes.append(Class("Class 1 - Forgen Smith", "1"))
    classes.append(Class("Class 1 - Forgen Smith", "3"))
    classes.append(Class("Class 1 - Forgen Smith", "5"))
    classes.append(Class("Class 2 - Hawken", "50"))
    classes.append(Class("Class 2 - Hawken", "69"))
    classes.append(Class("Class 2 - Hawken", "23"))
    
    nodes = request_location_info(classes)
    return render_template('map.html', nodes=nodes) 

def get_path_info():
    return render_template('index.html') 

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return get_path_info()
    elif request.method == 'POST':
        return display_map()
    else:
        return "This shouldn't happen"

if __name__ == "__main__":
    
    app.run(debug=True)
