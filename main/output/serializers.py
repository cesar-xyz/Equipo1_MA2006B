from rest_framework import serializers
from .models import Output


class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = "__all__"
        read_only_fields = 'out_auditor'
