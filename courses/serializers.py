from rest_framework import serializers
from .models import Course
from django.core.exceptions import ObjectDoesNotExist


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "code", "name"]

    def validate(self, attrs):
        user = self.context.get('request', None).user
        institution = user.institution
        code = attrs.get('code', None)

        try:
            obj = Course.objects.get(code=code, institution=institution)
            raise serializers.ValidationError('This course already exists at {0}'.format(institution.name))
        except ObjectDoesNotExist:
            return attrs

