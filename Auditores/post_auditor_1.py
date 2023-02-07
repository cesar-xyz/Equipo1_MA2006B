# import socket
import hashlib
import json
import time

# Libreria de los pines de la raspberry
import RPi.GPIO as GPIO
import pandas as pd
import requests
from ecdsa import SigningKey, NIST256p
from getmac import get_mac_address as gma

LED_PIN = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


# funcion para hashear objetos
def hash_dict(d):
    hash_string = ""
    for key, value in sorted(d.items()):
        hash_string += str(key) + str(value)
    return hashlib.sha256(hash_string.encode()).hexdigest()


# obtener direccion MAC
mac = gma()

ip_receptor = "192.168.100.28"

# urls del CCpost_auditor_1.py
url_entries = "https://192.168.100.28:8000/api/v1/entries/"
url_certificates = "https://192.168.100.28:8000/api/v1/certificates/"
url_public_keys = "https://192.168.100.28:8000/api/v1/public_keys/"
url_auditors = "https://192.168.100.28:8000/api/v1/auditors/"
url_outputs = "https://192.168.100.28:8000/api/v1/out_auditors/"

headers = {
    'Content-Type': 'application/json'
}

# autenticacion de CC
auth = ('admin@cocoa.com', '1234')

response_certificates = requests.get(url_certificates, auth=auth, verify=False)

auditor_name = "Auditor 1"
auditor_pk = 0
publicKey_pk = 0
algorithm = "ECDSA NIST256p"
existe_certificado = False

# creando las llaves de firmado
sk = SigningKey.generate(curve=NIST256p)

# private key
signing_key_hex_string = sk.to_string().hex()

if response_certificates.status_code == 200:
    json_certificates = response_certificates.json()
    for data in json_certificates:
        try:
            if data["auditor"]["name"] == auditor_name:
                auditor_pk = int(data["auditor"]["id"])
                existe_certificado = True

                # public key
                verifying_key_hex_string = data['public_key']['public_key']
                break
            else:
                print(" ")
        except:
            print("Name key not found in auditor dictionary.")

    if not existe_certificado:

        # public key
        verifying_key_hex_string = sk.verifying_key.to_string().hex()

        response_auditor = requests.get(url_auditors, auth=auth, verify=False)
        response_publicKey = requests.get(url_public_keys, auth=auth, verify=False)

        json_auditor = {'name': auditor_name, 'mac_address': mac}
        response_auditor = requests.post(url_auditors, json=json_auditor, headers=headers, auth=auth, verify=False)

        json_auditor = response_auditor.json()
        for data in json_auditor:
            try:
                if data['name'] == json_auditor['name']:
                    auditor_pk = int(data["id"])
            except:
                print("Auditor not found.")

        json_publicKey = {'algorithm': algorithm, 'public_key': verifying_key_hex_string}
        response_publicKey = requests.post(url_public_keys, json=json_publicKey, headers=headers, auth=auth,
                                           verify=False)

    # leer el documento de la base de datos de consumo

    df0 = pd.read_csv("../Archivos_trazas/auditor1.csv")
    df0['auditor'].replace(df0['auditor'][0], auditor_pk, inplace=True)
    df1 = df0
    for i in range(500):
        response_output = requests.get(url_outputs, auth=auth, verify=False)
        json_output = response_output.json()
        for data in json_output:
            try:
                if data["auditor"] == auditor_pk:
                    if data["message"] == '1':
                        print("Upload")
                        GPIO.output(LED_PIN, GPIO.HIGH)
                    elif data["message"] == '2':
                        print("Shutdown")
                        GPIO.output(LED_PIN, GPIO.LOW)
                    elif data["message"] == '3':
                        print("Disconnect")
                    else:
                        print("Message null")
            except:
                print("Name key not found in auditor dictionary.")

        # agregado de la direccion MAC a la base de datos
        df0.loc[i, 'mac_emisor'] = mac
        df0.loc[i, 'ip_receptor'] = ip_receptor
        # convirtiendo a objeto JSON cada entrada
        payload = df0.iloc[i].to_json()
        jpayload = json.loads(payload)

        # hasheando el objeto JSON
        if 'signature' in jpayload:
            del jpayload['signature']
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
        response = requests.post(url_entries, json=new_jpayload, headers=headers, auth=auth, verify=False)
        print(response.status_code)
        # separacion de tiempo de 0.15 segundos para no saturar el sistema
        time.sleep(.15)
