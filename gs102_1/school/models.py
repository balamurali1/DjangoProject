from django.db import models


# Create your models here.

#MultiTable Inheritance(one to one relation)
#Superclass or Base class or Parent class

class ExamCenter(models.Model):
	cname = models.CharField(max_length = 70)
	city = models.CharField(max_length = 70)


#sub class or chaild class
class Student(ExamCenter):
	name = models.CharField(max_length = 70)
	roll = models.IntegerField()
