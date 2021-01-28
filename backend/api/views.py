from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PingSerializer
from .models import Ping

# Viewsets base class provids all CRUD implementations by default. All we have to do is  specify the serializer class and query set


class PingView(viewsets.ModelViewSet):
    serializer_class = PingSerializer
    queryset = Ping.objects.all()
