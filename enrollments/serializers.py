from rest_framework import serializers
from .models import Enrollment
from django.core.exceptions import ObjectDoesNotExist


class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = ["id", "user", "course", "muted"]

