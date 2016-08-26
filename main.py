import os.path, requests, json
from flask import Flask, request
app = Flask(__name__)

class Class(object):
    def __init__(self, name, buildingNumber):
        self.name = name
        self.buildingNumber = buildingNumber

def fetch_data():
    if not os.path.isfile("/locations.cache"):
        locationFile = open("location.cache", "w")
        r = requests.get("http://uqmaps.app.uq.edu.au/json/locations")
        # strip unnecessary info

        locationFile.write(r.text)
        locationFile.close()

    # Read from file now

    locationFile = open("location.cache", "r")
    data = json.loads(locationFile.read())
    return data
    
def request_location_info(latitude, longitude):
    data = fetch_data()
    pass

def display_map():
    class1 = Class("Class 1 - Forgen Smith", 1)
    class2 = Class("Class 2 - Hawken", 50)

    return request_location_info(0, 0)
    pass

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
