# UQ Route

[Website](http://uqroute.com)

UQ Route is a simple web service that from a list of user inputted building (in sequential order), generates a path around UQ using Google Maps API to generate the map and path.



# Running locally

To run this locally you need atleast Python 3.4, and all the dependicies within `Requirements.txt` (install using pip).

From there simply run the Flask app using `python application.py` in the root directory. By default this hosts the app on `127.0.0.1:5000`. You will also need to get your own [Google Maps API Key](https://developers.google.com/maps/documentation/javascript/) and place it in the javascript url at the
bottom of the `map.html` file.
