from django.shortcuts import render, HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("This is home page")

def exceptionpage(request):
    a = 10/0
    return a