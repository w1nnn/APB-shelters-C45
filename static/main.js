window.onload = init();

function init() {
  const coordinates = ol.proj.transform(
    [119.428038, -5.153766],
    "EPSG:4326",
    "EPSG:3857"
  );

  let map = new ol.Map({
    target: "jsmap",
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM(),
      }),
    ],
    view: new ol.View({
      center: coordinates,
      zoom: 17,
    }),
  });

  // Layer untuk berbagai jenis peta
  const openStreetMapStandard = new ol.layer.Tile({
    source: new ol.source.OSM(),
    visible: false,
    title: "OSM_Standard",
  });

  const openStreetMapHumanitarian = new ol.layer.Tile({
    source: new ol.source.OSM({
      url: "https://{a-c}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
    }),
    visible: true, // Set default visible to true
    title: "OSM_Humanitarian",
  });

  const StamenTerrain = new ol.layer.Tile({
    source: new ol.source.XYZ({
      url: "http://tile.stamen.com/terrain/{z}/{x}/{y}.jpg",
    }),
    visible: false,
    title: "Stamen_Terrain",
  });

  const baseLayerGroup = new ol.layer.Group({
    layers: [openStreetMapHumanitarian, openStreetMapStandard, StamenTerrain],
  });

  map.addLayer(baseLayerGroup);

  // Base layer switcher
  let baseLayer = document.querySelectorAll(".navbar > input[type=radio]");
  for (let base of baseLayer) {
    base.addEventListener("change", () => {
      let select = base.value;
      baseLayerGroup.getLayers().forEach(function (element) {
        let bltitle = element.get("title");
        element.setVisible(bltitle === select);
      });
    });
  }

  const FillStyle = new ol.style.Fill({ color: [84, 118, 255, 1] });
  const StrokeStyle = new ol.style.Stroke({
    color: [46, 45, 45, 1],
    width: 2,
  });
  const CircleStyle = new ol.style.Circle({
    fill: new ol.style.Fill({ color: [249, 49, 5, 1] }),
    radius: 7,
    stroke: StrokeStyle,
  });

  const RouteGeoJson = new ol.layer.Vector({
    source: new ol.source.Vector({
      url: "data.geojson",
      format: new ol.format.GeoJSON(),
    }),
    visible: true,
    title: "route",
    style: new ol.style.Style({
      fill: FillStyle,
      stroke: StrokeStyle,
      image: CircleStyle,
    }),
  });

  map.addLayer(RouteGeoJson);

  map.on("click", function (e) {
    console.log(e.coordinate);
  });
}
