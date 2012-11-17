var io = require('socket.io').listen(8080);

sockets = [];

// we need to limit it to a time
io.sockets.on('connection', function (socket) {
  // add the socker
  // sockets.push(socket);

  //socket.emit('news', { hello: 'world', key:'value' });

  socket.on('init', function (data) {
    console.log(data.lon);
    console.log(data.lat);
    console.log(data.time);
    console.log(data.id);

    socket._lon = data.lon;
    socket._lat = data.lat;
    socket._time = data.time;
    socket._id = data.id;

    sockets.push(socket);

    // now lets look for a match and then
    socket.emit('result', { hello: 'world', key:'value' });

    socket.emit('result', { hello: 'world', key:'value' });

  });
  socket.on('disconnect', function () {
    // remove the socket
    //
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
