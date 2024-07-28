import secrets
from flask import Flask, render_template, request, Response
import sqlite3


app = Flask(__name__)

flag = open("./flag.txt").read()

db = sqlite3.connect(":memory:")
db.execute("drop table if exists users")
db.execute("""
           create table if not exists users (
           id int, 
           name varchar(255), 
           password varchar(255), 
           token varchar(255),
           message varchar(255)
)""")
db.execute(f"insert into users values (1, 'admin', '{secrets.token_hex(32)}', '{secrets.token_hex(32)}', '{flag}');")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["post"])
def login():
    username = request.form.get('username', default='', type=str)
    password = request.form.get('password', default='', type=str)
    token = request.headers.get('Token', '')
    users = db.execute(f"select name from users where name=? and password=? or token='{token}'", [username, password]).fetchall()
    if users:
        return Response(users[0][0], mimetype='text/plain')
    return Response('Login failed', mimetype='text/plain')
