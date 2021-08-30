from django import forms

class StudentRegistration(forms.Form):
	name = forms.CharField(label = "Your Name",label_suffix = ' ',
		initial = 'Sonam', required = False,help_text = "Limit 70 Char")
	email = forms.EmailField(disabled = True) #by default ga required = True,kani danini False cheyaliante required = False pettali
	'''
	mobile = forms.IntegerField()
	key = forms.CharField(widget = forms.HiddenInput())
	'''
	