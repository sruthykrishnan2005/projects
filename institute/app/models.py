from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default="General")

    def __str__(self):
        return self.title
