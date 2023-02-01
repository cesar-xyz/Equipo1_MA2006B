import socket
import time
import pandas as pd
import requests
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 8000))
IPAddr = s.getsockname()[0]

url = "https://0.0.0.0:8000/api/v1/entries/"

headers = {
    'Content-Type': 'application/json'
}

auth = ('admin@cocoa.com', '1234')

df0 = pd.read_csv("../Archivos_trazas/auditor0.csv")
for i in range(10):
    df0.loc[i, 'ip_emisor'] = IPAddr
    payload = df0.iloc[i].to_json()
    jpayload = json.loads(payload)
    response = requests.post(url, json=jpayload, headers=headers, auth=auth, verify=False)
    print(response.status_code)
    print(response.text)
    time.sleep(.15)
