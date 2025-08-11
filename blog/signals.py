from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, post_init, pre_save, post_save, pre_delete,post_delete
from .models import Blog
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