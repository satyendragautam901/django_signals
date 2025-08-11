from django.dispatch import Signal, receiver

# create signal
notification = Signal()

# send notification
@receiver(notification)
def custom_signal(sender, **kwargs):
    print("******* custom signal *****")
    print("sender: ", sender)
    print(f'kwargs {kwargs}')
