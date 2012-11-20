var io = require('socket.io').listen(80);

sockets = [];

var DEBUG = true;
// we need to limit it to a time
io.sockets.on('connection', function (socket) {

  socket.on('init', function (data) {
    if(DEBUG){
      console.log(data.lon);
      console.log(data.lat);
      console.log(data.time);
      console.log(data.id);
    }

    socket._lon = data.lon;
    socket._lat = data.lat;
    socket._time = data.time;
    socket._id = data.id;

    var match = false;
    // now lets look for a match and then
    for (var i = 0; i < sockets.length; i++) {
      var diff = distance(sockets[i]._lat, sockets[i]._lon,socket._lat, socket._lon);
      // 1 km
      if (diff<1){
        if(DEBUG)
          console.log("*\n*\n"+diff+"\n");
        socket.emit('found', { id:sockets[i]._id});
        match = true;
        socket.disconnect();
        break;
      }
    }
    if (!match){
      if(DEBUG)
        console.log("no match");
      socket.emit('looking', { key:"no-match"});
      sockets.push(socket);
    }

  });

  socket.on('disconnect', function () {
    // remove the socket
    var i = sockets.indexOf(socket);
    console.log(sockets[i] + " is gone away!");
    sockets.splice(i, 1);
    io.sockets.emit('user disconnected');
  });

});


function distance(lat1, lon1, lat2, lon2) {
	var radlat1 = Math.PI * lat1/180;
	var radlat2 = Math.PI * lat2/180;
	var radlon1 = Math.PI * lon1/180;
	var radlon2 = Math.PI * lon2/180;
	var theta = lon1-lon2;
	var radtheta = Math.PI * theta/180;
	var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
	dist = Math.acos(dist);
	dist = dist * 180/Math.PI;
	dist = dist * 60 * 1.1515;
	dist = dist * 1.609344;
	return dist;
}
