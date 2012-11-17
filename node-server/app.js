var io = require('socket.io').listen(8080);

sockets = [];

io.sockets.on('connection', function (socket) {
  sockets.push(socket);

  socket.emit('news', { hello: 'world', key:'value' });

  socket.on('my other event', function (data) {
    console.log(data);
  socket.emit('result', { hello: 'world', key:'value' });

  });
  socket.on('disconnect', function () {
    io.sockets.emit('user disconnected');
  });

});
