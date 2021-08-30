from django.db import models
from . managers import CustomManager

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 70)
	roll = models.IntegerField()

	objects = models.Manager() #objects is by default
	students = CustomManager() # students i created manuvally
	