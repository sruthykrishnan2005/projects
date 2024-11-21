from django.shortcuts import render
from.models import Course

def home(request):
    if 'home' in request.session:
        data=Course.objects.all()
        return render(request,'institutes/home.html',{'course':data})
    else:
        return redirect(request, 'institutes/sample.html')

def about(request):
    return render(request, 'institutes/about.html')

def contact(request):
    return render(request, 'institutes/contact.html')
