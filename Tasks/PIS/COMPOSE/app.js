const http = require("http");

http.createServer((request, response) => {
    console.log(`Request to app on port ${process.env.PORT}, request:${request.url}`)
    response.end(`Hello world Message for you: ${process.env.HELLO_MESSAGE}`);
}).listen(process.env.PORT || 3000, ()=> {console.log(`Our app should be running on port ${process.env.PORT}`)});