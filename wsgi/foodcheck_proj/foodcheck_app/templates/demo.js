L.Map.include(L.LayerIndexMixin);

var map = L.map('map');
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);
map.fitWorld();
map.addControl(new L.Control.Information());

for (var i=0; i<5000; i++) {
    var lat = Math.random() * 170 - 85
      , lng = Math.random() * 350 - 175;
    var layer = L.circleMarker(L.latLng([lat, lng])).setRadius(1).addTo(map);
    map.indexLayer(layer);
}

map.fire('moveend');

