from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    cname = models.TextField()
    dis=models.TextField()
    img=models.FileField()
    

class Contact(models.Model):
    name = models.TextField()
    phone_number = models.TextField() 
    email = models.EmailField()