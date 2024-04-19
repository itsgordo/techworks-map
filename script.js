function myFunc(counties) {
  // Initialize map
  var map = L.map("map").setView([42.10442, -75.91277], 10  );

  // Add tile layer
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution:
      '&copy; <a href="http://www.openstreetmap.org  /copyright">OpenStreetMap</a>',
  }).addTo(map);

  // Set map bounds and limits
  var southWest = L.latLng(41.59588, -77.45020),
    northEast = L.latLng(42.9885729, -75.1574637);
  var bounds = L.latLngBounds(southWest, northEast);
  map.setMaxBounds(bounds);
  map.on("drag", function () {
    map.panInsideBounds(bounds, { animate: false });
  });
  map.setMinZoom(map.getBoundsZoom(map.options.maxBounds));

  // Add marker at Techworks
  var marker = L.marker([42.10442, -75.91277]).addTo(map);
  marker.bindPopup("<b>Techworks!</b><br>");

  // County Label Options
  var labelOptions = {
    permanent: true,
    direction: "center",
    className: "my-labels",
  };

  // Active County Options
  var activeCountiesOptions = {
    fillColor: "#ff9933",
    color: "black",
    weight: 2,
    fillOpacity: 0.3,
  };

  // Hover Active County Options
  var hoverActiveCountiesOptions = {
    weight: 3,
    fillOpacity: 0.7,
  };

  // Non-Active County Options
  var nonActiveCountiesOptions = {
    fillColor: "grey",
    color: "grey",
    weight: 2,
  };

  var popUpOptions = {
    maxWidth: calculatePopupMaxWidth(), // Calculate max width dynamically
    width: calculatePopupWidth(), // Calculate width dynamically
    className: "popupCustom",
  };

  // Function to calculate the popup max width based on screen size
  function calculatePopupMaxWidth() {
    // Set the maximum width as a percentage of the window width
    var maxWidthPercentage = 0.9; // Adjust this value as needed
    var maxWidth = window.innerWidth * maxWidthPercentage;
    // Return the calculated maximum width as a string
    return maxWidth.toString() + "px";
  }

  // Function to calculate the popup width based on screen size
  function calculatePopupWidth() {
    // Set the width as a percentage of the window width or a fixed value
    var widthPercentage = 0.8; // Adjust this value as needed
    var width = window.innerWidth * widthPercentage;

    // Return the calculated width as a string
    return width.toString() + "px";
  }

  // Function to calculate the max width of the image based on screen size
  function calculateImageMaxWidth() {
    // Set the maximum width of the image as a percentage of the window width
    var imageMaxWidthPercentage = 0.8; // Adjust this value as needed
    var imageMaxWidth = window.innerWidth * imageMaxWidthPercentage;

    // Return the calculated maximum width as a string
    return imageMaxWidth.toString() + "px";
  }

  // Function to update label sizes based on zoom level
  function updateLabelSize() {
    var currentZoom = map.getZoom();
    var labelSize;

    if (currentZoom <= 10) {
      labelSize = "10px";
    } else if (currentZoom <= 12) {
      labelSize = "12px";
    } else {
      labelSize = "14px";
    }

    // Update label style with new font size
    document.querySelectorAll(".my-labels").forEach(function (label) {
      label.style.fontSize = labelSize;
    });
  }

  // Initial call to set label sizes
  updateLabelSize();

  // Listen for zoom events and update label sizes accordingly
  map.on("zoomend", updateLabelSize);

  // Adds counties to map
  L.geoJson(counties, {
    style: function (feature) {
      if (feature.properties.active) {
        return activeCountiesOptions;
      } else {
        return nonActiveCountiesOptions;
      }
    },
    onEachFeature: onEachFeature,
  }).addTo(map);

  // Mouseover actions
  function onMapMouseOver(e) {
    var layer = e.target;

    // Hover highlight if the county is active
    if (layer.feature.properties.active) {
      layer.setStyle(hoverActiveCountiesOptions);
      layer.bringToFront();
      info.update(layer.feature.properties);
    }
  }

  // Resets mouseover actions
  function onMapMouseOut(e) {
    var layer = e.target;

    // Reset hover highlight if the county is active
    if (layer.feature.properties.active) {
      layer.setStyle(activeCountiesOptions);
      info.update();
    }
  }

  // Click actions
  function onMapClick(e) {
    var layer = e.target;

    // Info pop Up on clicked county
    if (layer.feature.properties.active) {
      var popupContent =
        "<h3><b>" + layer.feature.properties.name + " Historical Society</b></h3>" +
        "<img src='" + layer.feature.properties.image +
          "' style='max-width: " + calculateImageMaxWidth() + "; height: 200px;' border='2px solid transparent';>" +
        "<h4><b>Website: </b><a href='" + layer.feature.properties.website + "'>" + layer.feature.properties.website + "</a></h4>" +
        "<h4><b>Address: </b>" + layer.feature.properties.address + "</h4>" +
        "<h4><b>Phone: </b>" + layer.feature.properties.phone +
        "</h4>" + "<a href='" + layer.feature.properties.website + "'><button>Visit Website</button></a>";

      // Create popup with specified options
      var popup = L.responsivePopup(popUpOptions).setContent(popupContent);

      // Bind popup to layer
      layer.bindPopup(popup);

      // Open popup
      layer.openPopup();
    }
  }

  // Event listeners
  function onEachFeature(feature, layer) {
    // Label counties
    layer.bindTooltip(feature.properties.name, labelOptions);

    layer.on({
      mouseover: onMapMouseOver,
      mousedown: onMapMouseOver,
      mouseup: onMapMouseOut,
      mouseout: onMapMouseOut,
      click: onMapClick,
    });
  }

  // Top Right info box
  var info = L.control();

  info.onAdd = function (map) {
    this._div = L.DomUtil.create("div", "info"); // create a div with a class "info"
    this.update();
    return this._div;
  };

  // Method that we will use to update the control based on feature properties passed
  info.update = function (props) {
    this._div.innerHTML =
      "<h4>County</h4>" +
      (props
        ? "<b>" + props.name + "</b><br />"
        : "Click on a county for more info");
  };

  info.addTo(map);
}

// Get data from counties JSON file
fetch("counties.json")
  .then((data) => data.json())
  .then((counties) => myFunc(counties));
