class FourDigitYearConverter:
	regex = '[0-9]{4}' #4 = ante 4digites matrame enter cheyali ani artham.


	def to_python(self,value):
		return int(value)

	def to_url(self,value):
		return f'{value:4d}'	#4d=ante 4 Digites ani artham
			#(OR)
		#return '%4d' % value	