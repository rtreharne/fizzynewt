from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from institutions.models import Institution

def get_institution_from_email_domain(email):
    institutions = Institution.objects.all()
    email_domain = "@" + email.split("@")[1]
    for institution in institutions:
        if email_domain in institution.email_domain:
            return institution
    else:
        return None

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('Users should have a username.')

        if email is None:
            raise TypeError('Users should have an email.')

        institution = get_institution_from_email_domain(email)

        user = self.model(username=username, email=self.normalize_email(email), institution=institution)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError('The password should not be none')

        user = self.create_user(username, email, password)
        user.is_super = True
        user.is_staff = True

        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    institution = models.ForeignKey(to=Institution, on_delete=models.PROTECT, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

