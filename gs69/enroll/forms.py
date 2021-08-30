from django import forms
from . models import User

class StudentRegistration(forms.ModelForm):
	class Meta:
		model = User
		#fields = ['name','password','email']

			#field format changed.
		#fields = ['name','email','password']

					#(OR)

			#___all__ ante models.py lo unde 'field name' format lo vasthundi. 
		#fields = '__all__'

			#exclude ante "field's" ni remove chesthundi.
		exclude = ['name']
			#(OR)

			#tuple lo rasthe last ku 'comma' pettali
		#exclude = ('name',)	