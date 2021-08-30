from django.db import models
 
# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 70,blank = True) #balnk = True,pedithey error message kanapadadu.
	email = models.EmailField(max_length = 100,blank = True)
	password = models.CharField(max_length = 100, blank = False) 