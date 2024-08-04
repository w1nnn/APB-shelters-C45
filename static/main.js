window.onload = init();

function init() {
  const coordinates = ol.proj.transform(
    [119.428038, -5.153766],
    "EPSG:4326",
    "EPSG:3857"
  );

  // Membuat instance peta
  let map = new ol.Map({
    target: "jsmap",
    layers: [], // Mulai dengan tanpa layer
    view: new ol.View({
      center: coordinates,
      zoom: 17,
    }),
  });

  // Membuat layer untuk OSM Standard
  const openStreetMapStandard = new ol.layer.Tile({
    source: new ol.source.OSM(),
    visible: false,
    title: "OSM_Standard",
  });

  // Membuat layer untuk OSM Humanitarian
  const openStreetMapHumanitarian = new ol.layer.Tile({
    source: new ol.source.OSM({
      url: "https://{a-c}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
    }),
    visible: true, // Default layer yang ditampilkan
    title: "OSM_Humanitarian",
  });

  // Membuat layer untuk Stamen Terrain
  const stamenTerrain = new ol.layer.Tile({
    source: new ol.source.XYZ({
      url: "http://tile.stamen.com/terrain/{z}/{x}/{y}.jpg",
    }),
    visible: false, // Default tidak ditampilkan
    title: "Stamen_Terrain",
  });

  // Mengelompokkan layer
  const baseLayerGroup = new ol.layer.Group({
    layers: [openStreetMapStandard, openStreetMapHumanitarian, stamenTerrain],
  });

  map.addLayer(baseLayerGroup); // Menambahkan kelompok layer ke peta

  // Event listener untuk mengganti layer ketika link diklik
  const layerLinks = document.querySelectorAll(".navbar a");
  layerLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault(); // Menghindari perilaku default link
      const selectedLayer = link.getAttribute("data-layer");

      // Mengubah visibilitas layer
      baseLayerGroup.getLayers().forEach(function (element) {
        const bltitle = element.get("title");
        element.setVisible(bltitle === selectedLayer); // Mengubah visibilitas layer
      });
    });
  });
}
