# UQ Route

[Website](http://uqroute.com)

UQ Route is a simple web service created with Flask to provide pathing around UQ, right now the web application generates a path around UQ using OpenSourceMaps, using libraries/APIs leafletjs, Mapbox, leaflet-routing-machine and Mapzen. This project was originally created at [UQCS Hackathon 2016](https://uqcs.org.au/).

# Future Features
- A better alternative to UQNav
- Different display options for the route
- Android/iOS specific implementations
- Statistics for routes
- Support for interiors of buildings (with multiple levels)
- Better front end

# Running locally

To run this locally you need atleast Python 3.4, pip and all the dependicies within `Requirements.txt` (install using pip). Using the keys in `map.html` shouldn't be a problem since both services are free with very generous limits. If you're develping your own application/change the appearance of the map it's probably best to generate your own keys: [Mapbox](https://mapbox.com/) and [Mapzen](https://mapzen.com/).

From there simply run the Flask app using `python application.py` in the root directory. By default this hosts the app on `127.0.0.1:5000`.
