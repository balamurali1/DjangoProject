from django.db import models


# Create your models here.

#Note:proxy ante ne Base class,chaild class Behaviours same untai.base class yooka 
	#filed's chaild class ki apply auvthai.

class ExamCenter(models.Model):
	cname = models.CharField(max_length = 70)
	city = models.CharField(max_length = 70)

class MyExamCenter(ExamCenter):
	class Meta:
		proxy =True
		#ordering = ['id'] #passitive pedithey 1,2,3,4,...	
		#ordering = ['-id'] #negative pedithey 4,3,2,1....
		ordering = ['city']