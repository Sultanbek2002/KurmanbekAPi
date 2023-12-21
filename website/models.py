from django.db import models

# Create your models here.
class Director(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Teacher(models.Model):
    name=models.CharField(max_length=200)
    great=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Student(models.Model):
    name=models.CharField(max_length=200)
    great=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
