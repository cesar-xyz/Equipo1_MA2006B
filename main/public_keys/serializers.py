from rest_framework import serializers
from public_keys.models import PublicKey


class PublicKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicKey
        fields = "__all__"
