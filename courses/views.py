from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CourseSerializer
from .models import Course
from rest_framework import permissions

class CourseListAPIView(ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.all()

class CourseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.all()
