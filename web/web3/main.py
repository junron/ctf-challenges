from flask import Flask, request, render_template, Response
import yaml

app = Flask(__name__)
assert yaml.__version__ == "5.3.1"

@app.route("/")
def index():
    return render_template("./index.html")
    
@app.route("/", methods=["POST"])
def welcome():
    student_data = request.form.get("student_data")
    if not student_data:
        return Response("Please specify some data in YAML format", mimetype='text/plain')
    student_data = yaml.load(student_data)
    required_fields = ["id","name","class"]
    if type(student_data) != dict or "student" not in student_data or any(x not in student_data["student"] for x in required_fields):
        return Response("Malformed data. Please try again.", mimetype='text/plain')
    student = student_data["student"]
    return f"<h1>Welcome, {student['name']} ({student['id']})</h1> <br>Your class is <b>{student['class']}</b>"


    
    
