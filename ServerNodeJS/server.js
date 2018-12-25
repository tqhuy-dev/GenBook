const http = require('http');
const request = require('request');
const port = process.env.port || 3000;
const app = require('./app')
const server = http.createServer(app);
// const constant  = require('./common/constant');
server.listen(port , function(){
    console.log('Express server is listening port:' + port);
});
