function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition);
	} else {
		alert("Geolocation is not supported by this browser.");
	}
}

function showPosition(position) {
	var latitude = position.coords.latitude;
	var longitude = position.coords.longitude;
	var timestamp = position.timestamp;
	send(longitude, latitude, timestamp);
}

function submit() {
	x.innerHTML = "data sent";
}

