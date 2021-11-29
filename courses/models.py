from django.db import models
from institutions.models import Institution

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date = models.DateField(auto_now_add=True)
    duration = models.FloatField(default=12)
    institution = models.ForeignKey(to=Institution, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('code', 'institution')

    def __str__(self):
        return self.code
