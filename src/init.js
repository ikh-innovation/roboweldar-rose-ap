const http = require('http');
const hello = require('./hello');

http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end(hello.getText().join(' '));
}).listen(8080);
