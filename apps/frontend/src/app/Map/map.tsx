import React, { useEffect } from 'react';
import { LatLngTuple } from 'leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import 'leaflet-routing-machine';

interface MapProps {
  waypoints?: LatLngTuple[];
  admin: boolean;
  location: LatLngTuple;
}

const Map: React.FC<MapProps> = ({ waypoints, admin=false, location }) => {

  useEffect(() => {
  
    const mapContainer = document.getElementById('map');

    if (!mapContainer) return;

    if (mapContainer.hasChildNodes()) {
      mapContainer.removeChild(mapContainer.firstChild as Node);
    }

    const map = L.map('map').setView(location, 17);
    map.removeControl(map.attributionControl);
    map.removeControl(map.zoomControl);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    let control;
    if (waypoints){
      if (admin) {
        control = createAdminRoutingControl(map, waypoints);
      } else {
        control = createUserRoutingControl(map, waypoints);
      }  
    }
    
    if (control) {
      control._container.style.display = 'none';
    }

    return () => {
      map.remove();
    };
  }, []);

  const createAdminRoutingControl = (map: any, waypoints: LatLngTuple[]) => {
    const L = require('leaflet');

    const startIcon = new L.Icon({
      iconUrl: 'circle-dot.svg',
      iconSize: [25, 41],
      iconAnchor: [12, 25],
    });

    const waypointIcon = new L.Icon({
      iconUrl: 'garbage.svg',
      iconSize: [32, 32],
      iconAnchor: [16, 16],
    });

    return L.Routing.control({
      waypoints: waypoints.map((wp) => L.latLng(wp[0], wp[1])),
      createMarker: function (this: any, i: number, wp: { latLng: LatLngTuple }, nWps: number) {
        const icon = i === 0 ? startIcon : waypointIcon;
        return L.marker(wp.latLng, {
          icon: icon,
          draggable: false,
        });
      },
    }).addTo(map);
  };

  const createUserRoutingControl = (map: any, waypoints: LatLngTuple[]) => {
    const L = require('leaflet');

    const startIcon = new L.Icon({
      iconUrl: 'circle-dot.svg',
      iconSize: [25, 41],
      iconAnchor: [12, 25],
    });

    const endIcon = new L.Icon({
      iconUrl: 'garbage.svg',
      iconSize: [25, 41],
      iconAnchor: [12, 41],
    });

    return L.Routing.control({
      waypoints: waypoints.map((wp, index) => L.latLng(wp[0], wp[1])),
      createMarker: function (i: number, wp: { latLng: LatLngTuple }, nWps: number) {
        const icon = i === 0 ? startIcon : endIcon;
        return L.marker(wp.latLng, { icon: icon, draggable: false });
      },
    }).addTo(map);
  };

  return <div id="map" className="w-full h-full z-0"></div>;
};

export default Map;
