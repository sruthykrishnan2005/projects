from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    cname = models.TextField()
    dis=models.TextField()
    img=models.FileField()