from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PingSerializer, LogListSerializer
from .models import Ping, Log

# Viewsets base class provids all CRUD implementations by default. All we have to do is  specify the serializer class and query set


class PingView(viewsets.ModelViewSet):
    serializer_class = PingSerializer
    queryset = Ping.objects.all()

class LogView(viewsets.ModelViewSet):
    serializer_class = LogListSerializer
    queryset = Log.objects.all()