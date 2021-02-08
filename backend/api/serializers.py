# Serialiszers act as a bridge between Pythonic data structures and the API

from rest_framework import serializers
from .models import Ping, Log

class PingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ping
        fields = ('id', 'title', 'description', 'completed')

class LogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('course', 'newt_code', 'session_type', 'start', 'finish', 'message')


