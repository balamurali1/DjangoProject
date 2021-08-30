from django import forms

class StudentRegistration(forms.Form):
	name = forms.CharField()  #name(dinini field name antaru) = %s
	email = forms.EmailField() #email(dinini field name antaru) = %s
	first_name = forms.CharField() #first_name lo underscore(_) esthe chrome lo underscore ni "space"ga convert chesukuntundi.

