from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PingSerializer, NewtSerializer, InstitutionSerializer
from .models import Ping, Newt, Institution

# Viewsets base class provids all CRUD implementations by default. All we have to do is  specify the serializer class and query set


class PingView(viewsets.ModelViewSet):
    serializer_class = PingSerializer
    queryset = Ping.objects.all()

class NewtView(viewsets.ModelViewSet):
    serializer_class = NewtSerializer
    queryset = Newt.objects.all()

class InstitutionView(viewsets.ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()