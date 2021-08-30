from . models import Page
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete,sender= Page)
def delete_related_user(sender,instance,**kwargs):
	print("Page Post_Delete")
	instance.user.delete()

#Note:CASCADE/ikkada emity ante page ni delete chesinappudu page matrame delete auvthundi
		#user delete kadu.kada...alakakunda page ni delete chesthe user kuda delete kavali ante ele signals.py lo code rayali.