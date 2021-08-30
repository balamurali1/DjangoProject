from django import forms

class StudentRegistration(forms.Form):
	name = forms.CharField(initial = "Murali",help_text = "In This text area you will write 30 char")
	