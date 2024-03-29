import hashlib

from certificates.models import Certificate
from ecdsa import NIST256p, VerifyingKey
from public_keys.models import PublicKey
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .models import Entry
from .serializers import EntrySerializer


# funcion para hashear objetos
def hash_dict(d):
    hash_string = ""
    for key, value in sorted(d.items()):
        hash_string += str(key) + str(value)
    return hashlib.sha256(hash_string.encode()).hexdigest()


# Definir una clase EntryViewSet que gestiona los objetos Entry
class EntryViewSet(viewsets.ModelViewSet):
    # Asignar un queryset con todos los objetos Entry de la base de datos
    queryset = Entry.objects.all()
    # Asignar la clase EntrySerializer como el serializador utilizado por la clase
    serializer_class = EntrySerializer
    # Definir que los permisos necesarios para acceder a los métodos de la clase son estar autenticado
    permission_classes = [permissions.IsAuthenticated]

    # Método que se ejecuta antes de crear un nuevo objeto Entry
    def perform_create(self, serializer):
        # Obtener el nombre del auditor a partir de los datos enviados en la solicitud
        auditor = self.request.data.get('auditor')
        date = self.request.data.get('date')
        is_producing = self.request.data.get('is_producing')
        mac_emisor = self.request.data.get('mac_emisor')
        ip_receptor = self.request.data.get('ip_receptor')
        quantity = self.request.data.get('quantity')
        signa = self.request.data.get('signature')

        json_package = {"auditor": auditor, "date": date, "is_producing": is_producing, "quantity": quantity,
                        "mac_emisor": mac_emisor, "ip_receptor": ip_receptor}
        hashed = hash_dict(json_package)

        # Buscar el primer certificado asociado al auditor
        certificate = Certificate.objects.filter(auditor__id=auditor).first()
        pubObj = PublicKey.objects.get(id=certificate.public_key.pk)
        publiKey = pubObj.public_key

        verifyingkey = VerifyingKey.from_string(bytearray.fromhex(publiKey), curve=NIST256p)
        signature = bytearray.fromhex(signa)
        try:
            print('Verify transmited data', verifyingkey.verify(signature, hashed.encode('utf-8')))
        except:
            print(" ")

        # Comprobar si existe un certificado asociado al auditor
        if certificate:
            # Comprobar si el certificado ha caducado
            if certificate.check_expiry():
                # Guardar el nuevo objeto Entry
                serializer.save()
            else:
                # Lanzar una excepción ValidationError si el certificado ha caducado
                raise ValidationError("Certificate has expired.")
        else:
            # Lanzar una excepción ValidationError si no se encuentra un certificado asociado al auditor
            raise ValidationError("No matching certificate found for the given auditor_id")
