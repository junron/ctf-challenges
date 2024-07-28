import secrets
from flask import Flask, render_template, request, Response
import sqlite3
from flags import *

flag0 = "flag{you_can_use_automated_tools_like_nikto_to_do_this}"


app = Flask(__name__)

db = sqlite3.connect("./data.db")
db.execute(f"insert into users values (1, 'admin', '{flag2}');")


@app.route("/")
def index():
    def filter(obj):
        print([(k,v) for k,v in request.args.items()])
        return any([len(v) > 1 and k != 'q' for k, v in request.args.items()])
    print(request.args, filter(request.args))
    print(request.args['x'])
    return render_template("index.html")
    
@app.route("/robots.txt")
def robots():
    return Response("User-agent: *\nDisallow: /c7179ef35b2d458d6f2f68044816e145/main.py", mimetype='text/plain')

@app.route("/c7179ef35b2d458d6f2f68044816e145/main.py")
def source():
    return Response(open(__file__,"r").read(), mimetype='text/plain')

@app.route("/login", methods=["post"])
def login():
    username = request.form.get('username', default='', type=str)
    password = request.form.get('password', default='', type=str)
    users = db.execute(f"select id from users where name='{username}' and password='{password}'").fetchall()
    if users:
        return Response(flag1, mimetype='text/plain')
    return Response('Login failed', mimetype='text/plain')
