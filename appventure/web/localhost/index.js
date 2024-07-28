const http = require("http");
const url = require('url');

const host = '0.0.0.0';
const port = 8080;



const requestListener = function (req, res) {

    const remote = req.socket.remoteAddress;
    console.log(remote);
    if (remote === "127.0.0.1") {
        res.end(process.env.FLAG);
        return;
    }

    const queryObject = url.parse(req.url, true).query;
    const site = queryObject["site"];
    if (!site) {
        res.end("Give me a site and I'll fetch it for you!");
        return;
    }
    if (!site.startsWith("http://localhost")) {
        res.end("Only localhost is allowed!");
        return;
    }
    if (site.includes("localhost:") || site.includes("127.0.0.1")) {
        res.end("Localhost is not allowed!");
        return;
    }

    http.get(site, (resp) => {
        let data = '';
        resp.on('data', (chunk) => {
            data += chunk;
        });
        resp.on('end', () => {
            res.end(data);
        });

    }).on("error", (err) => {
        res.end("Error: " + err.message);
    });


};

const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});
