from rest_framework import serializers
from .models import School
from django.core.exceptions import ObjectDoesNotExist


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ["id", "name"]

    def validate(self, attrs):
        user = self.context.get('request', None).user
        institution = user.institution
        name = attrs.get('name', None)

        if institution is None:
            raise serializers.ValidationError('User is not associated with an institution')

        try:
            obj = School.objects.get(name=name, institution=institution)
            raise serializers.ValidationError('This school already exists at {0}'.format(institution.name))
        except ObjectDoesNotExist:
            return attrs