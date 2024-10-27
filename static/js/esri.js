require([
    "esri/Map", 
    "esri/views/MapView",
    "esri/widgets/Search",
    "esri/widgets/ScaleBar",
    "esri/layers/FeatureLayer"
], function(Map, MapView, Search, ScaleBar, FeatureLayer) {

    // Initialize the map
    var map = new Map({
        basemap: "streets-night-vector" // Choose a basemap
    });

    // Set up the map view
    var view = new MapView({
        container: "viewDiv", // Reference to the map's container (div element)
        map: map,              // Reference to the map object
        center: [-100.33, 43.69], // Longitude, latitude of map's center
        zoom: 3,                // Initial zoom level
        minZoom: 2
    });

    // Add a search widget
    var search = new Search({
        view: view
    });
    view.ui.add(search, "top-right");
    view.constraints.minZoom = 2

    // Add a scale bar widget
    var scaleBar = new ScaleBar({
        view: view
    });
    view.ui.add(scaleBar, "bottom-left");

    // Optional: Add a FeatureLayer if you want to display data on the map
    var featureLayer = new FeatureLayer({
        url: "https://services.arcgis.com/your-feature-layer-url"
    });
    map.add(featureLayer);

}); 


