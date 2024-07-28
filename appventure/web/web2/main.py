import secrets
from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route("/")
def index():
    name = request.args.get("name", default="World")
    # Evil hacker cannot get past now!
    blocklist = ["{{", "}}", "__", "subprocess", "flag", "popen", "system", "os", "import", "read", "flag.txt"]
    for bad in blocklist:
        name = name.replace(bad, "")
    return render_template_string(f"<h1> Hello, {name}")
    
    