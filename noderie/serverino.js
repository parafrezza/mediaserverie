var portaDaCuiAscoltare = 30000;
var host = "127.0.0.1";

var dgram = require('dgram');

var server = dgram.createSocket('udp4');

server.on('listening', function()
{
    console.log( "ciao, sono in ascolto " + server.address().address + " sulla porta " + server.address().port);   

});

server.on('message', function(message, remote)
{
    console.log( "ciao, ho ricevuto " + message + " da " + remote.address);   
    
});

server.bind(portaDaCuiAscoltare, host);