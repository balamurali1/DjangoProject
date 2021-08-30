from django import forms
from . models import User


class StudentRegistration(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name','email','password']
		labels = {'name' : 'Enter Name','email':'Enter Email','password':'Enter Password'}
		error_messages = {'name':{'required':'please enter correct name'},
		'email':{'required':'please enter correct email_id'},
		'password':{'required':'please enter correct password'}}	 
		widgets = {
		'password':forms.PasswordInput,
		'name':forms.TextInput(attrs = {'class':'myclass','placeholder' :'Enter name'}),
		'email':forms.TextInput(attrs = {'class':'myclass','placeholder' :'Enter email'}),
		'password':forms.TextInput(attrs = {'class':'myclass','placeholder' :'Enter password'})}