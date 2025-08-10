from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

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