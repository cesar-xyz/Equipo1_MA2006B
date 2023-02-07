#import socket
from getmac import get_mac_address as gma
import time
import pandas as pd
import requests
import json
import hashlib
from ecdsa import SigningKey, VerifyingKey, NIST256p

'''s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 8000))
IPAddr = s.getsockname()[0]'''

# obtener direccion MAC
mac = gma()

# url del CC
url = "https://0.0.0.0:8000/api/v1/entries/"

headers = {
    'Content-Type': 'application/json'
}

# autenticacion de CC
auth = ('admin@cocoa.com', '1234')

# funcion para hashear objetos
def hash_dict(d):
    hash_string = ""
    for key, value in sorted(d.items()):
        hash_string += str(key) + str(value)
    return hashlib.sha256(hash_string.encode()).hexdigest()

# creando las llaves de firmado
sk = SigningKey.generate(curve=NIST256p)
# private key
signing_key_hex_string = sk.to_string().hex()
# public key
verifying_key_hex_string = sk.verifying_key.to_string().hex()

# LINEAS DE CODIGO PARA VERIFICAR LAS FIRMAS
''' 
verifyingkey = VerifyingKey.from_string(bytearray.fromhex(verifying_key_hex_string), curve=NIST256p)
signature = bytearray.fromhex(signature_hex_string)
print('Verify transmited data', verifyingkey.verify(signature, hashed.encode('utf-8')))
'''

# leer el documento de la base de datos de consumo
df0 = pd.read_csv("../Archivos_trazas/auditor0.csv")
for i in range(10):
    # agregado de la direccion MAC a la base de datos
    df0.loc[i, 'mac_emisor'] = mac
    # convirtiendo a objeto JSON cada entrada
    payload = df0.iloc[i].to_json()
    jpayload = json.loads(payload)
    # hasheando el objeto JSON
    hashed = hash_dict(jpayload)

    # creando la firma
    sk = SigningKey.from_string(bytearray.fromhex(signing_key_hex_string), curve=NIST256p)
    signature = sk.sign(hashed.encode('utf-8'))
    signature_hex_string = signature.hex()

    # payload final (incluye la firma)
    df0.loc[i, 'signature'] = signature_hex_string
    new_payload = df0.iloc[i].to_json()
    new_jpayload = json.loads(new_payload)

    # enviar la informacion al CC
    response = requests.post(url, json=new_jpayload, headers=headers, auth=auth, verify=False)
    print(response.status_code)
    print(response.text)
    # separacion de tiempo de 0.15 segundos para no saturar el sistema
    time.sleep(.15)
