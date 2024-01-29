import requests, json

data = [{
  "username": "deneme",
  "password": "12345"
}]

response = requests.post(
  "http://localhost:2552/api/1MbDMJRWk-C_G0MBDBngR0H4RKc4vDx-6K946xmUcXIk/deneke",
  headers={"Accept": "application/json", "Content-Type": "application/json"},
  data=json.dumps(data)
)

print(data)

if response.ok:
  # İstek başarılı oldu.
  print(response.json())
else:
  # İstek başarısız oldu.
  print(response.status_code)

data = [3, {"username": "yasir", "password": "54321"}]

response = requests.patch(
  "http://localhost:2552/api/1MbDMJRWk-C_G0MBDBngR0H4RKc4vDx-6K946xmUcXIk/deneke",
  headers={"Accept": "application/json", "Content-Type": "application/json"},
  data=json.dumps(data)
)

print(data)

if response.ok:
  # İstek başarılı oldu.
  print(response.json())
else:
  # İstek başarısız oldu.
  print(response.status_code)

data = [3]

response = requests.delete(
  "http://localhost:2552/api/1MbDMJRWk-C_G0MBDBngR0H4RKc4vDx-6K946xmUcXIk/deneke",
  headers={"Accept": "application/json", "Content-Type": "application/json"},
  data=json.dumps(data)
)

print(data)

if response.ok:
  # İstek başarılı oldu.
  print(response.json())
else:
  # İstek başarısız oldu.
  print(response.status_code)

# res = requests.post("https://script.google.com/macros/s/AKfycbwSelNU95tE8vzZMOaOsdwvyvyjUGK5zCEX_3SrhFS2tkgg7dq6FkRhDbodY4BIJQMByw/exec?id=1MbDMJRWk-C_G0MBDBngR0H4RKc4vDx-6K946xmUcXIk&type=delete&sheet=accounts&row=3", headers={"Accept": "application/json", "Content-Type": "application/json"}, data="aa")

# print(res.text)

