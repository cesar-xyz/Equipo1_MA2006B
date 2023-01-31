import requests

url = "https://0.0.0.0:8000/api/v1/entries/"

payload = {
    "auditor": "Au1",
    "date": "15",
    "is_producing": "False",
    "quantity": "25.4",
    "ip_emisor": "null",
    "ip_receptor": "null",
    "public_key": "null"
}

headers = {
    'Content-Type': 'application/json'
}

auth = ('admin@cocoa.com', '1234')

response = requests.post(url, json=payload, headers=headers, auth=auth, verify=False)

print(response.status_code)
print(response.text)
