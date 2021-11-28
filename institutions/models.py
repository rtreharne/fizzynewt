from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email_domain = models.CharField(max_length=255, blank=True, default=None)

    def __str__(self):
        return self.name
