from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *


class userApiView(APIView):
    def get(self,request):
        allUsers = user.objects.all().values()
        return Response({"messages":"list of users","user list":allUsers})
        
    def post(self,request):
        user.objects.create(name=request.data['name'],password=request.data['password'])
        return Response({"messages":"NewBook Added","user":user})

        

# Create your views here.
