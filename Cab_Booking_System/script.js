// Handle tab switching
function showTab(tabId) {
  const tabs = document.querySelectorAll('.tab-content');
  tabs.forEach(tab => tab.style.display = 'none');
  document.getElementById(tabId).style.display = 'block';
}

// Default tab
document.addEventListener("DOMContentLoaded", () => {
  showTab('ongoing');
});

// Initialize Google Maps
function initMap() {
  const center = { lat: 28.6139, lng: 77.2090 }; // Delhi coordinates
  const map = new google.maps.Map(document.getElementById("mapPlaceholder"), {
    zoom: 12,
    center: center,
  });

  // Example marker (replace with live data later)
  new google.maps.Marker({
    position: center,
    map: map,
    title: "Cab Location"
  });
}
