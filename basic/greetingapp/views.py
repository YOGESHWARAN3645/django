from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    hello='<h1>Hello world</h1>'
    return HttpResponse(hello)

def morning(request): 
    return HttpResponse('<h1>Hello Friend Good Morning!!!</h1>') 
def evening(request): 
    return HttpResponse('<h1>Hello Friend Good Evening !!!</h1>') 
def afternoon(request): 
    return HttpResponse('<h1>Hello Friend Good Afternoon!!!</h1>')

# Create your views here.
