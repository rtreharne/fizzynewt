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
        return serializer.save(institution = self.request.user.institution)

    def get_queryset(self):
        return self.queryset.filter(institution=self.request.user.institution)

class CourseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"


    def get_queryset(self):
        return self.queryset.filter(institution=self.request.user.institution)
