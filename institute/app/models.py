from django.db import models

class Course(models.Model):
    """
    Model for storing navigation bar links.
    """
    cname = models.TextField()
    dis=models.TextField()
    img=models.FileField()