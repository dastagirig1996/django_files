from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length = 20)
    course = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    address = models.TextField(max_length = 30)