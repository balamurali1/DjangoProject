from django.db import models

# Create your models here.

class Student(models.Model): 	#Student(is the Table name)
	stuid = models.IntegerField()
	stuname = models.CharField(max_length = 70)
	stuemail = models.EmailField(max_length = 70)
	stupass = models.CharField(max_length = 70)