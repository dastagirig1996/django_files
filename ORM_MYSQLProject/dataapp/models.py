from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.emp_name