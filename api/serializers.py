# Serialiszers act as a bridge between Pythonic data structures and the API

from rest_framework import serializers
from .models import Ping

class PingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ping
        fields = ('id', 'title', 'description', 'completed')

