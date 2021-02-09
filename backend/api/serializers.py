# Serialiszers act as a bridge between Pythonic data structures and the API

from rest_framework import serializers
from .models import Ping, Newt, Institution

class PingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ping
        fields = ('id', 'title', 'description', 'completed')

class NewtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newt
        fields = ('course', 'newt_code', 'session_type', 'start', 'finish', 'message')

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'country')



