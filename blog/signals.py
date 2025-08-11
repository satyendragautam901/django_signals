from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import (pre_init, post_init, 
                                      pre_save, post_save, 
                                      pre_delete,post_delete,
                                      pre_migrate, post_migrate)
from .models import Blog
from django.core.signals import request_finished, request_started, got_request_exception
from django.db.backends.signals import connection_created
# user logged signal

@receiver(user_logged_in, sender = User)# you can also use connect method but receive is more handy
def login_signls(sender, request, user, **kwargs):
    print("**************")
    print("User logged Signal")
    print("User name: ", user.username)
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user)
    print(f'kwargs: {kwargs}')
# user_logged_in.connect(login_signals, sender = User) # this can be use in place of receiver

# user logged out signal
@receiver(user_logged_out, sender = User)
def logout_signal(sender, request, user, **kwargs):
    print("**************")
    print("User logged Out Signal")
    print("User name: ", user.username)
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user)
    print(f'kwargs: {kwargs}')

# login failed signals
@receiver(user_login_failed)
def logout_signal(sender, credentials, request, **kwargs):
    print("**************")
    print("User login failed Signal")
    print("Sender: ", sender)
    print("Request: ", request)
    print("Credentials: ", credentials)
    print(f'kwargs: {kwargs}')

# models signals
@receiver(pre_save, sender=Blog)  # pre_save signal, sender will be the model to listen to (Blog in this case)
def presave_signal(sender, instance, raw, using, update_fields, **kwargs):
    print("**************")
    print("Pre Save Signal")
    print("Sender: ", sender)  # The model class (Blog) that triggered the signal
    print("Instance: ", instance)  # The actual model instance (e.g., the Blog object being saved)
    print("Raw: ", raw)  # Boolean indicating whether the model is being saved in raw form (default is False)
    print("Using: ", using)  # The database alias being used (e.g., 'default' if no custom DB is specified)
    print("Update fields: ", update_fields)  # List of fields being updated, or None if saving all fields
    print(f'kwargs: {kwargs}')  # Any additional keyword arguments passed to the signal (usually empty)

@receiver(post_save, sender = Blog) # post save signal
def postsave_signal(sender, instance,created, raw, using, update_fields, **kwargs):
    if created: # if new record then this will run otherwise next one
        print("**************")
        print("Post Save Signal")
        print("Sender: ", sender) 
        print("Instance: ", instance)  
        print("Raw: ", raw)  
        print("Using: ", using) 
        print("Update fields: ", update_fields)  
        print("Created: ", created) # if new instance is created then true otherwise false
        print(f'kwargs: {kwargs}')  

    print("**************")
    print("Post Save Signal")
    print("Sender: ", sender) 
    print("Instance: ", instance)  
    print("Raw: ", raw)  
    print("Using: ", using) 
    print("Update fields: ", update_fields)  
    print("Created: ",created)
    print("Updated record ") 
    print(f'kwargs: {kwargs}') 

# delete signal
@receiver(pre_delete, sender = Blog) # pre delete signal
def predelete_singal(sender, instance, **kwargs):
    print("**************")
    print("Pre delete Signal")
    print("Sender: ", sender) 
    print("Instance: ", instance)
    print(f'kwargs: {kwargs}') 

@receiver(post_delete, sender = Blog) # post delete signal
def postdelete_singal(sender, instance, **kwargs):
    print("**************")
    print("Post delete Signal")
    print("Sender: ", sender) 
    print("Instance: ", instance)
    print(f'kwargs: {kwargs}') 

# pre and posts init signals
@receiver(pre_init, sender = Blog)
def preinit_signal(sender, args, **kwargs):
    print("**************")
    print("Pre Init Signal")
    print("Sender: ", sender) 
    print("Args: ", args)
    print(f'kwargs: {kwargs}') 

@receiver(post_init, sender = Blog)
def postinit_signal(sender, *args, **kwargs):
    print("**************")
    print("Post Init Signal")
    print("Sender: ", sender) 
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}') 

# request/response signals

@receiver(request_started) # request started signal
def requeststarted_signal(sender, environ, **kwargs):
    print("**************")
    print("Request started Signal")
    print("Sender: ", sender) 
    print("Envion: ", environ)
    print(f'kwargs: {kwargs}')

@receiver(request_finished) # request finished signal
def requeststarted_signal(sender, **kwargs):
    print("**************")
    print("Request finished Signal")
    print("Sender: ", sender) 
    print(f'kwargs: {kwargs}')

@receiver(got_request_exception) # request got exception signal
def requestgotexception_signal(sender,request, **kwargs):
    print("**************")
    print("Request got exception Signal")
    print("Sender: ", sender) 
    print("Request: ", request)
    print(f'kwargs: {kwargs}')

# pre and post migrate
@receiver(pre_migrate)
def premigrate_signal(sender, app_config, verbosity, interactive
                      ,using, plan, apps, **kwargs):
    print("****** Pre migrate Signal ******")
    print("Sender: ", sender) 
    print("App config : ", app_config)
    print("verbosity: ", verbosity)
    print("Interactive: ", interactive)
    print("Using: ", using)
    print("plan: ",plan)
    print("apps: ", apps)
    print(f'kwargs: {kwargs}')

@receiver(post_migrate)
def premigrate_signal(sender, app_config, verbosity, interactive
                      ,using, plan, apps, **kwargs):
    
    print("****** Post migrate Signal ******")
    print("Sender: ", sender) 
    print("App config : ", app_config)
    print("verbosity: ", verbosity)
    print("Interactive: ", interactive)
    print("Using: ", using)
    print("plan: ",plan)
    print("apps: ", apps)
    print(f'kwargs: {kwargs}')

# databse connection signal
@receiver(connection_created)
def dbconnectsignal(sender, connection, **kwargs):
    print("****** Database connection Signal ******")
    print("Sender: ", sender) 
    print("Connection: ",connection)
    print(f'kwargs: {kwargs}')