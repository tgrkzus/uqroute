import os.path, requests, json, sys
from flask import Flask, request, redirect
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
        nLat = str(data[i.buildingNumber]["latitude"])
        nLong = str(data[i.buildingNumber]["longitude"])
        nodePath.append([nName, nLat, nLong])
    # Generate node url
    url = "https://www.google.com.au/maps/dir"
    for i in nodePath:
        url += "/" + i[1] + "," + i[2]

    return redirect(url)

def display_map():
    classes = []
    classes.append(Class("Class 1 - Forgen Smith", "1"))
    classes.append(Class("Class 2 - Hawken", "50"))

    return request_location_info(classes)

def get_path_info():
    return '''
            <form action="" method="post">
            <input type="text" name="Course">
            <input type="text" name="Building">
            <input type="text" name="Time">
            <br>
            <input type="submit" value=Select>
            </form>
        ''' 

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return get_path_info()
    elif request.method == 'POST':
        return display_map()
    else:
        return "This shouldn't happen"

if __name__ == "__main__":
    app.run()
