function createMap(input) {
    // Decode input:
    

    var node = L.latLng(-27.4989042, 153.0131141);

    var map = L.map('map').setView([-27.4989042, 153.0131141], 13);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18,
            id: 'tgrkzus.18862nnb',
            accessToken: 'pk.eyJ1IjoidGdya3p1cyIsImEiOiJjaXNlbjZkaHowMGI4MnlydDk0cTI1aXZxIn0.baEJ-39wtc9AkyxDebjQHQ'
            }).addTo(map);

    var router = L.Routing.mapzen('valhalla-KAduFrX', {costing:"pedestrian"});
    var control = L.Routing.control({
        router: router,
        formatter: new L.Routing.mapzenFormatter(),
        waypoints: node
    }).addTo(map);

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
