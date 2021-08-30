from django.contrib.auth.signals import user_logged_in,user_logged_out, user_login_failed
from django.contrib.auth.models import User  #User is the 'sender' okay
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete,pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created



#user_logged_in

#Note Ex: This function is 'reciver function'
@receiver(user_logged_in,sender = User)
def login_success(sender,request,user,**kwargs):
	print("-------------------------------")
	print("Logged-in Signal..Run Intro...")
	print("Sender:",sender)
	print("Request:",request)
	print("User:",user)
	print("User Password:",user.password)
	print(f'kwargs:{kwargs}')
#Note:signal-->connect method-->(reciver function--->User)
#user_logged_in.connect(login_success,sender = User)


 #user_logged_out
@receiver(user_logged_out,sender = User)
def log_out(sender,request,user,**kwargs):
	print("-------------------------------")
	print("Logged-out Signal..Run Outro...")
	print("Sender:",sender)
	print("Request:",request)
	print("User:",user)
	print(f'kwargs:{kwargs}')
#user_logged_out.connect(log_out,sender = User)


#user_login_failed
@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
	print("-------------------------------")
	print("Login Failed Signal.....")
	print("Sender:",sender)
	print("Credentials:",credentials)
	print("Request:",request)
	print(f'kwargs:{kwargs}')
#user_login_failed.connect(login_failed)	



#pre_save
@receiver(pre_save,sender = User)
def at_beginning_save(sender,instance,**kwargs):
	print("-------------------------------")
	print("Pre Save Signal.....")
	print("Sender:",sender)
	print("Instance:",instance)
	print(f'kwargs:{kwargs}')
#pre_save.connect(at_beginning_save,sender = User)



#post_save
@receiver(post_save,sender = User)
def at_ending_save(sender,instance, created,**kwargs):
	if created:
		print("-------------------------------")
		print("post Save Signal.....")
		print("New Record")
		print("Sender:",sender)
		print("Instance:",instance)
		print("Created:",created)
		print(f'kwargs:{kwargs}')
	else:
		print("-------------------------------")
		print("Post Save Signal.....")
		print("Update Record")
		print("Sender:",sender)
		print("Instance:",instance)
		print("Created:",created)
		print(f'kwargs:{kwargs}')		
#post_save.connect(at_ending_save,sender = User)


#pre_delete
@receiver(pre_delete,sender = User)
def at_beginning_delete(sender,instance,**kwargs):
	print("-------------------------------")
	print("pre Delete Signal.....")
	print("Sender:",sender)
	print("Instance:",instance)
	print(f'kwargs:{kwargs}')
#pre_delete.connect(at_beginning_delete,sender = User)


#post_delete
@receiver(post_delete,sender = User)
def at_ending_delete(sender,instance,**kwargs):
	print("-------------------------------")
	print("post Delete Signal.....")
	print("Sender:",sender)
	print("Instance:",instance)
	print(f'kwargs:{kwargs}')
#post_delete.connect(at_ending_delete,sender = User)



#pre_init
@receiver(pre_init,sender = User)
def at_beginning_init(sender,*args,**kwargs):
	print("-------------------------------")
	print("pre init Signal.....")
	print("Sender:",sender)
	print(f'Args:{args}')
	print(f'kwargs:{kwargs}')
#pre_init.connect(at_beginning_init,sender = User)



#post_init
@receiver(post_init,sender = User)
def at_ending_init(sender,*args,**kwargs):
	print("-------------------------------")
	print("post init Signal.....")
	print("Sender:",sender)
	print(f'Args:{args}')
	print(f'kwargs:{kwargs}')
#post_init.connect(at_ending_init,sender = User)




#request_started
@receiver(request_started)
def at_beginning_request(sender,environ,**kwargs):
	print("-------------------------------")
	print("At Beginning Request.....")
	print("Sender:",sender)
	print('Environ:',environ)
	print(f'kwargs:{kwargs}')
#request_started.connect(at_beginning_request)


#request_finished
@receiver(request_finished)
def at_ending_request(sender,**kwargs):
	print("-------------------------------")
	print("At Ending Request.....")
	print("Sender:",sender)
	print(f'kwargs:{kwargs}')
#request_finished.connect(at_ending_request)



#got_request_exception
@receiver(got_request_exception)
def at_req_exception(sender,request,**kwargs):
	print("-------------------------------")
	print("At Request Exception.....")
	print("Sender:",sender)
	print('Request:',request)
	print(f'kwargs:{kwargs}')
#got_request_exception.connect(at_req_exception)


#pre_migrate
@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
	print("----------------------------")
	print("before_install_app.....")
	print('Sender:',sender)
	print('App_config:',app_config)
	print('Verbosity:',verbosity)
	print('Interactive:',interactive)
	print('Using:',using)
	print('Plan:',plan)
	print('App:',apps)
	print(f'kwargs:{kwargs}')
#pre_migrate.connect(before_install_app)	



#post_migrate
@receiver(post_migrate)
def at_end_migrate_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
	print("----------------------------")
	print("at_end_migrate_flush.....")
	print('Sender:',sender)
	print('App_config:',app_config)
	print('Verbosity:',verbosity)
	print('Interactive:',interactive)
	print('Using:',using)
	print('Plan:',plan)
	print('App:',apps)
	print(f'kwargs:{kwargs}')
#post_migrate.connect(at_end_migrate_flush)


#connection_created
@receiver(connection_created)
def conn_db(sender,connection,**kwargs):
	print("----------------------------")
	print("Initial connection to the database.......")
	print('sender:',sender)
	print('Connection:',connection)
	print(f'kwargs:{kwargs}')
#connection_created.connect(conn_db)	



