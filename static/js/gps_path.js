var control = {};
var target  = {};

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


    var control = {};
    var prevLayer = {};
    map.locate({setView: false, watch: true})
        .on('locationfound', function(e){
            var marker = L.marker([e.latitude, e.longitude]).bindPopup('User location');

        map.removeLayer(prevLayer);
        map.addLayer(marker);
        prevLayer = marker;

        repath(L.latLng(e.latitude, e.longitude));
        })
    .on('locationerror', function(e){
        console.log(e);
    });       

    var router = L.Routing.mapzen('valhalla-KAduFrX', {costing:"pedestrian"});
    control = L.Routing.control({
        router: router,
        formatter: new L.Routing.mapzenFormatter(),
    });
    control.addTo(map);

    //var distance = 0;
    //router.route(control.getWaypoints(), function(err, routes) {
    //    for (var i = 0; i < routes.length; i++) {
    //        distance += routes[i].summary.totalDistance;
    //    }
    //}

    //document.getElementById('distance').innerHTML = distance;
    //document.getElementById('calories').innerHTML = distance / 1000 * 70;

    //for (var i = 0; i < nodes.length; ++i) {
    //    L.marker(nodes[i]).addTo(map);
    //}

}


function repath(loc) {
    control.setWaypoints([loc, target]);
    control.route();
}
