from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache


#Login's countings.....
@receiver(user_logged_in,sender = User)
def login_success(sender,request,user,**kwargs):
	ct = cache.get('count',0,version = user.pk) #pk ante 'id' ni thisukuntundi,0is default valye,'count' is key
	newcount = ct + 1
	cache.set('count',newcount,60*60*24,version = user.pk)
	print(user.pk)
#Note:signal-->connect method-->(reciver function--->User)	
#user_logged_in.connect(login_success,sender = User)
	