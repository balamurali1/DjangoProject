from django.db import models

class CustomManager(models.Manager): #ikkada super() ante "Manager" ani artham
	def get_queryset(self):
		return super().get_queryset().order_by('name')