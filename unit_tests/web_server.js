// static web server to verify network connections work as intended
var http = require('http');

let port = 80;

http.createServer(function (req, res) {
    console.log(req.url);
    res.write('Hello World!');  //write a response to the client
    res.end();                  //end the response
}).listen(port);
