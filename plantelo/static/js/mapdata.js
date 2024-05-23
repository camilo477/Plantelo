var stateNamesById = {
    COL1316: "Córdoba",
    COL1317: "Santander",
    COL1314: "Antioquia",
    COL1315: "Boyacá",
    COL1318: "La Guajira",
    COL1422: "Casanare",
    COL1420: "Arauca",
    COL1421: "Norte de Santander",
    COL1408: "Valle del Cauca",
    COL1423: "Guaviare",
    COL1424: "Guainía",
    COL1425: "Meta",
    COL1426: "Vaupés",
    COL1427: "Vichada",
    COL1402: "Tolima",
    COL1403: "Caquetá",
    COL1400: "Quindío",
    COL1401: "Risaralda",
    COL1406: "Nariño",
    COL1407: "Putumayo",
    COL1404: "Cauca",
    COL1405: "Huila",
    COL1342: "San Andrés y Providencia",
    COL1283: "Amazonas",
    COL1398: "Cundinamarca",
    COL1399: "Bogotá",
    COL1415: "Chocó",
    COL1414: "Cesar",
    COL1417: "Sucre",
    COL1416: "Magdalena",
    COL1397: "Caldas",
    COL1413: "Bolívar",
    COL1412: "Atlántico"
};

var simplemaps_countrymap_mapdata={
    main_settings: {
     //General settings
      width: "700", //'700' or 'responsive'
      background_color: "#000000",
      background_transparent: "yes",
      border_color: "#000000",
      state_description: "",
      state_color: "#acf3a1",
      state_hover_color: "#5aba43",
      state_url: "",
      border_size: 1.5,
      all_states_inactive: "no",
      all_states_zoomable: "yes",
      
      //Location defaults
      location_description: "Location description",
      location_url: "",
      location_color: "",
      location_opacity: 0.8,
      location_hover_opacity: 1,
      location_size: 25,
      location_type: "square",
      location_image_source: "frog.png",
      location_border_color: "#FFFFFF",
      location_border: 2,
      location_hover_border: 2.5,
      all_locations_inactive: "no",
      all_locations_hidden: "no",
      
      //Label defaults
      label_color: "#d5ddec",
      label_hover_color: "#d5ddec",
      label_size: 22,
      label_font: "Arial",
      hide_labels: "no",
      hide_eastern_labels: "no",
     
      //Zoom settings
      zoom: "yes",
      manual_zoom: "yes",
      back_image: "no",
      initial_back: "no",
      initial_zoom: "-1",
      initial_zoom_solo: "no",
      region_opacity: 1,
      region_hover_opacity: 0.6,
      zoom_out_incrementally: "yes",
      zoom_percentage: 0.99,
      zoom_time: 0.5,
      
      //Popup settings
      popup_color: "white",
      popup_opacity: 0.9,
      popup_shadow: 1,
      popup_corners: 5,
      popup_font: "12px/1.5 Verdana, Arial, Helvetica, sans-serif",
      popup_nocss: "no",
      
      //Advanced settings
      div: "map",
      auto_load: "yes",
      url_new_tab: "no",
      images_directory: "default",
      fade_time: 0.1,
      link_text: "View Website",
      popups: "detect",
      state_image_url: "",
      state_image_position: "",
      location_image_url: "",
    },
    
    state_specific:{
        COL1316: "Córdoba",
        COL1317: "Santander",
        COL1314: "Antioquia",
        COL1315: "Boyacá",
        COL1318: "La Guajira",
        COL1422: "Casanare",
        COL1420: "Arauca",
        COL1421: "Norte de Santander",
        COL1408: "Valle del Cauca",
        COL1423: "Guaviare",
        COL1424: "Guainía",
        COL1425: "Meta",
        COL1426: "Vaupés",
        COL1427: "Vichada",
        COL1402: "Tolima",
        COL1403: "Caquetá",
        COL1400: "Quindío",
        COL1401: "Risaralda",
        COL1406: "Nariño",
        COL1407: "Putumayo",
        COL1404: "Cauca",
        COL1405: "Huila",
        COL1342: "San Andrés y Providencia",
        COL1283: "Amazonas",
        COL1398: "Cundinamarca",
        COL1399: "Bogotá",
        COL1415: "Chocó",
        COL1414: "Cesar",
        COL1417: "Sucre",
        COL1416: "Magdalena",
        COL1397: "Caldas",
        COL1413: "Bolívar",
        COL1412: "Atlántico"
    },
    locations: {},
    labels: {},
    legend: {
      entries: []
    },
    regions: {},
  };
  
  document.addEventListener('DOMContentLoaded', function() {
    var ventanaAbierta = false;
    // Define la configuración del mapa
    var simplemaps_countrymap_mapdata = {
        // Aquí va tu configuración del mapa
    };
    function toggleVentana() {
        var ventana = document.getElementById("miVentana");
        // Verifica si la ventana ya está abierta
        if (!ventanaAbierta) {
            // Si no está abierta, abre la ventana
            ventana.classList.add("ventana-abierto");
            // Actualiza el estado para indicar que la ventana está abierta
            ventanaAbierta = true;
        }
    }
    // Agrega un listener para manejar el evento después de completarse el zoom en el mapa
    simplemaps_countrymap.hooks.zooming_complete = function() {
        // Obtiene el nivel de zoom actual
        var zoomLevel = simplemaps_countrymap.zoom_level;
        var zoomArea;
        
        // Determina qué parte del mapa se está zoomando según el nivel de zoom
        switch (zoomLevel) {
            case 'out':
                zoomArea = 'Todo el mapa';
                break;
            case 'region':
                zoomArea = 'Región';
                break;
            case 'state':
                zoomArea = 'Estado';
                
                // Obtenemos el ID del estado actual al que se hizo zoom
                var zoomedStateId = simplemaps_countrymap.zoom_level_id;

                // Buscamos el nombre del estado en el objeto stateNamesById
                var zoomedStateName = stateNamesById[zoomedStateId] || 'Desconocido';

                var zoomEvent = new CustomEvent('mapZoomed', { detail: zoomedStateName });
                document.dispatchEvent(zoomEvent);
                
                
                console.log('Se ha completado la acción de zooma en:', zoomArea, 'Nombre del estado:', zoomedStateName);
                if (!ventanaAbierta) {
                    toggleVentana();
                    // Actualiza el estado para indicar que la ventana está abierta
                    ventanaAbierta = true;
                }
                break;
            case 'manual':
                zoomArea = 'Zoom manual';
                break;
            default:
                zoomArea = 'Desconocido';
        }
        
        // Imprimir en la consola la acción de zoom
        console.log('Se ha completado la acción de zoom en:', zoomArea);
        // Puedes agregar aquí cualquier acción que desees realizar después de que se complete el zoom en el mapa
    };
  });