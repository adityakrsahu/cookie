from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Contact=models.IntegerField()
    Password=models.CharField(max_length=100)
