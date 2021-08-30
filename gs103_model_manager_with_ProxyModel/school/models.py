from django.db import models
from . managers import CustomManager

# Create your models here.

#Super class(),Base class()antaru
class Student(models.Model):
	name = models.CharField(max_length = 70)
	roll = models.IntegerField()

#Subclass(),Chaild class() antaru
class ProxyStudent(Student):
	students = CustomManager() #i am created
	class Meta:
		proxy =True
		ordering = ['name']	 