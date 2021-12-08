from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SchoolSerializer
from .models import School
from rest_framework import permissions

class SchoolListAPIView(ListCreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        institution = self.request.user.institution
        return serializer.save(institution=institution)

    def get_queryset(self):
        return self.queryset.filter(institution=self.request.user.institution)

class SchoolDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter(institution=self.request.user.institution)
