from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import EnrollmentSerializer
from .models import Enrollment
from rest_framework import permissions


class EnrollmentListAPIView(ListCreateAPIView):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user__institution=self.request.user.institution)

class EnrollmentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(user__institution=self.request.user.institution)