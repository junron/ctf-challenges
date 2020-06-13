const http = require("http");
const url = require('url');
const sqlite3 = require('sqlite3');
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const host = '0.0.0.0';
const port = 8080;

// ❌💾💽😔
const db = new sqlite3.Database(':memory:');




const requestListener = function (req, res) {
    // lmao no funny express tricks
    const queryObject = url.parse(req.url, true).query;
    const flag = queryObject["flag"];

    db.exec("DROP TABLE if exists flags");

    db.exec("CREATE TABLE flags (flag TEXT)");

    db.exec(`INSERT INTO flags values ('${process.env.FLAG}')`)

    if (!queryObject["path"]) {
        // Part 1
        if (!flag) {
            res.end("You must specify a flag!");
            return;
        }
        try {
            // This matches everything
            // :)
            if (flag.match(/^.+$/)) {
                res.end("lmao imagine giving free flags");
                return;
            }
        } catch (e) {
            // :(
            res.write(`Oops something bad happened: ${e.message}`);
        }

        // Im stealing your flags
        console.log(flag);

        db.all(`select * from flags where flag='${flag}';`, (err, rows) => {
            // Many rows, such wow
            res.end(JSON.stringify(rows));
        })

        // Wat's the diff anyway???
        db.exec(`select * from flags where flag='${flag}';`);
    } else {
        // Part 2

        // Very safe, taken from stackoverflow: https://security.stackexchange.com/a/123723/202826
        var safeSuffix = path.normalize(queryObject["path"]).replace(/^(\.\.(\/|\\|$))+/, '');
        // What if you make files here :thonk:
        var safeJoin = path.join('/tmp/', safeSuffix);

        // This part of the challenge is actually related to SQLite
        let secret = Buffer.from(process.env.FLAG2);
        if (fs.existsSync(safeJoin)) {
            // What?
            secret = fs.readFileSync(safeJoin);
        } else {
            res.write("Path does not exist!");
        }

        // Wipe any traces!
        require('child_process').execSync('rm -rf /tmp/*')

        // One time pad!!!!
        // Most secure!!1
        return res.end(Buffer.from(process.env.FLAG2).map((b, i) => b ^ secret[i]).toString('hex'));
    }
};

const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});
