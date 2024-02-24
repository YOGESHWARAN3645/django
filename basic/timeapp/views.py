from django.shortcuts import render
from django.http import HttpResponse
import datetime

def time(request):
    time = datetime.datetime.now()
    s='<h1> Current time is '+str(time) +'</h1>'
    return HttpResponse(s)

# Create your views here.
