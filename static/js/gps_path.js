var control = {};
var target  = {};
var prevLayer = {};

function createMap(input) {
    // Decode input:
    target = L.latLng(-27.4980000, 153.0131141);
    var map = L.map('map').setView([-27.4989042, 153.0131141], 13);
    L.control.locate().addTo(map);
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
    setInterval(get_geolocation, 3000, map)

    var router = L.Routing.mapzen('valhalla-KAduFrX', {costing:"pedestrian"});
    control = L.Routing.control({
        router: router,
        formatter: new L.Routing.mapzenFormatter(),
    });
    control.addTo(map);
}

function get_geolocation(map) {
    map.locate();
}

function location_found(e, map) {
    var marker = L.marker([e.latitude, e.longitude]).bindPopup('User location');

    map.removeLayer(prevLayer);
    map.addLayer(marker);
    prevLayer = marker;

    repath(L.latLng(e.latitude, e.longitude));
}

function repath(loc) {
    control.setWaypoints([loc, target]);
    control.route();
}
