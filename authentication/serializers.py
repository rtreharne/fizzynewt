from rest_framework import serializers
from .models import User
from institutions.models import Institution
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', None)
        username = attrs.get('username', None)

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters.')

        email_domains = []
        for institution in Institution.objects.all():
            email_domains.extend(''.join(institution.email_domain.split()).split(","))

        if "@" + email.split("@")[1] not in email_domains:
            print("@" + email.split("@")[1])
            print(email_domains)
            raise serializers.ValidationError('The email address is not valid.')

        return attrs

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']

class LoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=6, read_only=True)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)


    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', None)
        password = attrs.get('password', None)

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again.')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email not verified.')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }

class UserSerializer(serializers.ModelSerializer):
    #is_verified = serializers.BooleanField()
    #is_staff = serializers.BooleanField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_verified', 'is_staff']

    def validate(self, attrs):

        user = self.context.get('request', None).user
        institution = user.institution
        email = attrs.get('email', None)
        if email:
            attrs["institution"] = institution

            email_domain = "@" + email.split("@")[1]

            if email_domain in institution.email_domain:
                return attrs
            else:
                raise serializers.ValidationError('User email is not associated with {0}'.format(institution))
        return attrs


