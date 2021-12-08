from django.db import models
from institutions.models import Institution

class School(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('name', 'institution')

    def __str__(self):
        return self.name


