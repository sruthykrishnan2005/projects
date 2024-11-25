from django.db import models

class Course(models.Model):
    cname = models.TextField()
    dis=models.TextField()
    img=models.FileField()