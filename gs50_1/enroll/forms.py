from django import forms


class StudentRegistration(forms.Form):
	name = forms.CharField()  #'name' is the visible
	email = forms.EmailField() #'email' is the visible
	mobile = forms.IntegerField() #'mobile' is the visible
	key = forms.CharField(widget = forms.HiddenInput()) #'key' is the visible