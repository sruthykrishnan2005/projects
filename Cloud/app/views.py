from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User


# Create your views here.
def login(req):
    if req.method=='POST':
        Username=req.POST['username']
        Password=req.POST['password']
        data=authenticate(username=Username,password=Password)
        if data:
            login(req,data)
            return redirect(home)
        
        else:
            messages.warning(req, "invalid password")
            return redirect(login)
    else:
        return render(req,'login.html')


def logout(req):
    logout(req)
    return redirect(login)
    
    
def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=password)
            data.save()
        except:
            messages.warning(req,"email alreadyin use")
            return redirect(register)
        return redirect(login)
    else:
        return render(req,'register.html')
    
def home(req):
   return render(req,'home.html')
    
    
