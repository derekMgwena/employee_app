# employees/models.py

from django.db import models

class Employee(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    skills = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

