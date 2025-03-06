from django.shortcuts import render

# Create your views here.
from  django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import  authenticate

class UserView(View):
    def get(self,request,*args,**kwargs):
        # user = User.objects.create_user(kwargs.get("name"),'abc@abb.com','123456')
        # return HttpResponse(user.__str__())
        user = authenticate(username="joe",password="123456")
        print(user.has_perm("polls.add_album"))
        if user is not None:
            return  HttpResponse('get user')
        else:
            return  HttpResponse(None)