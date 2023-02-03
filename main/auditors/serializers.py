from rest_framework import serializers
from .models import Auditor


class AuditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditor
        exclude = ["is_authorized"]
