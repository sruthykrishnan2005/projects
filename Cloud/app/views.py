from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from .forms import Fileform
from .models import File
from django.contrib.auth.models import User


# Create your views here.
def e_login(req):
    if req.method=='POST':
        Username=req.POST['username']
        Password=req.POST['password']
        data=authenticate(username=Username,password=Password)
        if data:
            login(req,data)
            return redirect(home)
        
        else:
            messages.warning(req, "invalid password")
            return redirect(e_login)
    else:
        return render(req,'login.html')
    
        
def e_logout(req):
    logout(req)
    return redirect(e_login)
    
def register(req):
    if req.method=='POST':
        username=req.POST['uname']
        email=req.POST['email']
        password=req.POST['password']
        
        try:
            data=User.objects.create_user(first_name=username,email=email,username=email,password=password)
            data.save()
        except:
            messages.warning(req,"username already exist")
            return redirect(register)
        return redirect(e_login)
    else:
        return render(req,'register.html')
    
def view(req):
    files = File.objects.all()
    return render(req,'view.html',{'files':files})


def add(request):
    if request.method == 'POST' and request.FILES.get('file'):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')  
    else:
        form = FileForm()
    
    return render(request, 'add.html', {'form': form})

def home(req):
    return render(req, 'home')


