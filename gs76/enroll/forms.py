from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
		# note:wroser lo kanabade password label ni  change cheyali ante ela
	password2 = forms.CharField(label = 'Confirm Password(again)',
		widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
				# note:wroser lo kanabade email label ni  change cheyali ante ela
		labels = {'email':'Email'}