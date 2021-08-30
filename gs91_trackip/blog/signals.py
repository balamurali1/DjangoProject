from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver


#IP address ni find out cheyadam.
@receiver(user_logged_in,sender = User)
def login_success(sender,request,user,**kwargs):
	# print("--------------------------------")
	# print("Logged-in Signal...Run Intro")
	ip = request.META.get('REMOTE_ADDR')
	# print("Client IP:",ip)
	request.session['ip'] = ip #ikkada 'ip' ni session lo store cheshanu ela.