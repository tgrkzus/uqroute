import os.path, requests, json, sys
from flask import Flask, request
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
    
def request_location_info(latitude, longitude):
    data = fetch_data()
    return data

def display_map():
    class1 = Class("Class 1 - Forgen Smith", 1)
    class2 = Class("Class 2 - Hawken", 50)

    return request_location_info(0, 0)["58A"]["title"]

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
