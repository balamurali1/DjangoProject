from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#OneToOne relationship-->Ex:okka user 'okka page' ni matrame create chestadu/cheyali.
class Page(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE, 
		primary_key = True,related_name = 'mypage')  #related_name = 'mypage'

	page_name = models.CharField(max_length = 70)
	page_cat = models.CharField(max_length = 70)
	page_publish_date = models.DateField()

#ManyToOne relationship--->Ex:'okka user' 'Multiple post's ni create chestadu/cheyavachunu
class Post(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE,
		related_name = 'mypost')    #related_name = 'mypost'

	post_title = models.CharField(max_length = 70)
	post_cat = models.CharField(max_length = 70)
	post_publish_date = models.DateField()


#ManyToManyField--->Ex:okka 'user' chala songs ni padavachunu,okka 'song' ni chala user's padavachunu.(it's like to opposite process okay..)
class Song(models.Model):
	user = models.ManyToManyField(User,related_name = 'mysong')

	song_name =models.CharField(max_length = 70)
	song_duration = models.IntegerField()

	def written_by(self):
		return ",".join([str(p) for p in self.user.all()])
