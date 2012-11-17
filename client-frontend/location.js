var x=document.getElementById("buttonToRunScript");
function getLocation(){
	if (navigator.geolocation){
		navigator.geolocation.getCurrentPosition(showPosition)
	}
	else{
		x.innerHTML="Geolocation is not supported by this browser.";
	}
}
function showPosition(position){
	//code to handle position data here. 
	latitude = position.coords.latitude;
	longitude = position.coords.longitude;
	time = position.timestamp
}
