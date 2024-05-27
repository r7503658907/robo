from rest_framework import serializers
from .models import RoboData

class RoboDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoboData
        fields = ['id', 'status', 'created_at']