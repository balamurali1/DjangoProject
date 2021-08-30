from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
	#Note1:CASCADE/ante User ni delete chesthe Page kuda delete auvthundi
	#Note2:CASCADE/ante Direct ga Page ne delete cheste page matrame delete auvthndi.kani 'unser' delete kadu.
	user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key =True)
	page_name = models.CharField(max_length = 70)
	page_cat = models.CharField(max_length = 70)
	page_publish_date = models.DateField()

class Like(Page):
	page = models.OneToOneField(Page,on_delete = models.CASCADE,primary_key =True,parent_link = True)
	likes = models.IntegerField()


#Note:parent_link = True--->dini gurinchi cheppinadu ikkada
#Note: 'models' ante ne "multiple classes Inheritance" ani....	