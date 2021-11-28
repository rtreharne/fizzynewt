from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import InstitutionSerializer
from .models import Institution
from rest_framework import permissions

class InstitutionListAPIView(ListCreateAPIView):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.all()

class InstitutionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.all()
