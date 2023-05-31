import requests
import json

base_url = 'https://petstore.swagger.io/v2'
status = 'available'

res = requests.get(f"{base_url}/pet/findByStatus?status={status}", headers={'accept': 'application/json'})
print(res.status_code, 'GET')
print(res.json())


new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res = requests.post(f"{base_url}/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(new_pet))
print(res.status_code, "POST")
print(res.json())

old_pet = {
  "id": 9223372036854598942,
  "category": {
    "id": 0,
    "name": "Cat1"
  },
  "name": "Dogg1",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"}
res = requests.put(f'{base_url}/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(old_pet))
print(res.status_code, "PUT")
print(res.json())


petId = 9223372036854598942
res = requests.delete(f'{base_url}/pet/{petId}', headers={'accept': 'application/json'})
print(res.status_code, "DELETE")
print(res.json())