# UQ Route

[Website](https://uqroute.com)

UQ Route is a simple web service created with Flask to provide pathing around UQ, right now the web application generates a path around UQ using OpenSourceMaps, using libraries/APIs leafletjs, Mapbox, leaflet-routing-machine and Mapzen. This project was originally created at [UQCS Hackathon 2016](https://uqcs.org.au/).

# Future Features
- A better alternative to UQNav
- Different display options for the route
- Android/iOS specific implementations
- Statistics for routes
- Support for interiors of buildings (with multiple levels)
- Better front end

# Running locally

To run this locally you need atleast Python 3.4, pip and all the dependicies within `Requirements.txt` (install using pip). Using the API keys in `map.html` shouldn't be a problem since both services are free with very generous limits. Though if you're planning to develop your own application you should probably generate your own keys: [Mapbox](https://mapbox.com/) and [Mapzen](https://mapzen.com/).
