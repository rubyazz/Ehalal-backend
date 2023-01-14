from rest_framework import serializers

from .models import Code


class EcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = "__all__"