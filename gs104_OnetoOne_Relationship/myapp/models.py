from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
	#Note1:CASCADE/ante User ni delete chesthe Page kuda delete auvthundi
	#Note2:CASCADE/ante Direct ga Page ne delete cheste page matrame delete auvthndi.kani 'unser' delete kadu.
	user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key =True)
	
	#Note:PROTECT/ante User ni delete chesina, Page delete kakunda undali ante PROTECT use cheyali.
		#haa page user dwara create aindi kabatti haa user kuda delete kadu finall ga.

	#user = models.OneToOneField(User,on_delete = models.PROTECT,primary_key =True)
	
	#user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key =True,limit_choices_to = {'is_staff':True})

	page_name = models.CharField(max_length = 70)
	page_cat = models.CharField(max_length = 70)
	page_publish_date = models.DateField()
