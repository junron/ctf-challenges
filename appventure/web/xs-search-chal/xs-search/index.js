const http = require("http");
const url = require('url');

const host = '0.0.0.0';
const port = 8080;

const requestListener = function (req, res) {
    // Haha no XSS now!
    const csp = {"Content-Security-Policy":"default-src 'none'; script-src 'sha256-tlhLl/V70m+kJIIku9rBhJ1wBt+an6djcRVIKMU36kk='"};
    res.writeHead(200, { 'Content-Type': 'text/html', ...csp });

    res.end(`
    <html><body><script>
        (()=>{
            const site = (new URLSearchParams(location.search)).get("site");
            const favorite = localStorage.getItem("favorite_site");
            if(!site){
                localStorage.setItem("favorite_site", "AVCTF{not_the_flag}");
                document.write("Guess my favorite site and i'll give you the flag!");
                return;
            }else{
                if(site.length > 200){
                    document.write('Too long!!');
                    return;
                }
                const guesses = site.split(" ");
                for(const guess of guesses){
                    if(favorite.includes(guess)){
                        document.write('yep! '+site+' is a good guess!!');
                        return;
                    }
                }
                document.write('nope! :(');
            }
        })();
        </script></body></html>
    `)
};

const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});
