from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class File(models.Model):
    name=models.TextField()
    file=models.FileField()
    dis=models.TextField()