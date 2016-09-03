var control = {};
var tempLayer = L.layerGroup([
                            L.marker([-27.4980000, 153.0131141], {title: "One", opacity: 0})]);
var searchControl = {};
var target  = {};
var prevLayer = {};

var oldWaypoints = {};

function createMap() {
    // Decode input:
    target = L.latLng(-27.4980000, 153.0131141);
    var map = L.map('map').setView([-27.4989042, 153.0131141], 13);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18,
            id: 'tgrkzus.18862nnb',
            accessToken: 'pk.eyJ1IjoidGdya3p1cyIsImEiOiJjaXNlbjZkaHowMGI4MnlydDk0cTI1aXZxIn0.baEJ-39wtc9AkyxDebjQHQ'
            }).addTo(map);

    map.on('locationfound', function(e) {
        location_found(e, map);
    });
    get_geolocation(map);
    //setInterval(get_geolocation, 2000, map)

    // Create invisible search layer with geolocations for each building
    searchControl = new L.Control.Search({ layer: tempLayer, moveToLocation: function (latlng) {
        set_target(latlng);
    }});
    map.addControl(searchControl);    
    get_locations();

    
    var router = L.Routing.mapzen('valhalla-q549CZP', {costing:"pedestrian"});
    control = L.Routing.control({
        router: router,
        formatter: new L.Routing.mapzenFormatter()
    });
    control.addTo(map);
}

function get_locations() {
    $.getJSON($SCRIPT_ROOT + '/get_locations', {}, function(data) {
        var searchLayer = L.layerGroup();
    
        for (var key in data.result) {
            searchLayer.addLayer(L.marker([
                    data.result[key]["latitude"],
                    data.result[key]["longitude"]],
                    { title: data.result[key]["title"], opacity: 0 }));
        }
        searchControl.setLayer(searchLayer);
    });
}

function get_geolocation(map) {
    map.locate({watch: true});
}

function location_found(e, map) {
    var marker = L.marker([e.latitude, e.longitude]).bindPopup('User location');

    map.removeLayer(prevLayer);
    map.addLayer(marker);
    prevLayer = marker;

    repath(L.latLng(e.latitude, e.longitude));
}

function set_target(loc) {
    target = loc;
}

function repath(loc) {
    var nPoints = [loc, target];
    if (oldWaypoints.toString() == nPoints.toString()) {
        return;
    }
    control.setWaypoints([loc, target]);
    oldWaypoints = nPoints;
}
