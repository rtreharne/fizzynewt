from rest_framework import serializers
from .models import Institution


class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = ["id", "name", "email_domain"]