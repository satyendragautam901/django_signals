from django.shortcuts import render,HttpResponse
from .signals import notification
# Create your views here.
def home(request):
    notification.send(sender = None, request=request, user = ["sattut", "Bhai"])
    return HttpResponse("This is custom signal")