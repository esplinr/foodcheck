L.Control.Information = L.Control.extend({
    options: {
        position: 'bottomright',
    },

    onAdd: function (map) {
        this._container = L.DomUtil.create('div', 'leaflet-control-attribution');
        L.DomEvent.disableClickPropagation(this._container);

        map.on('moveend', function (e) {
            if (map._loaded) {
                var shown = map.search(map.getBounds());
                console.log(map.getBounds().toBBoxString());
                this._container.innerHTML = shown.length + ' objects shown.';
            }
        }, this);
        return this._container;
    },

    onRemove: function (map) {
        map.off('moveend');
    },
});
