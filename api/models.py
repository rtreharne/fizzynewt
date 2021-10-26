from django.db import models
from regex_field.fields import RegexField

# Test model to check the API works
class Ping(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Institution(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class EmailSubstring(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    substring = models.CharField(max_length=128)

    def __str__(self):
        return self.substring

class IdFormat(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    regex = RegexField(max_length=128)

    def __str__(self):
        return str(self.regex)

class CourseCodeFormat(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    regex = RegexField(max_length=128)

    def __str__(self):
        return str(self.regex)

class Course(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.code

class UserType(models.Model):
    type = models.CharField(max_length=16)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.type

class User(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    user_id = RegexField(max_length=128)

    def __str__(self):
        return self.last_name

class SessionType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Log(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    newt_code = models.CharField(max_length=128)
    session_type = models.ForeignKey(SessionType, on_delete=models.PROTECT)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    message = models.TextField(max_length=10000, default=False, null=True)

    def __str__(self):
        return self.course






