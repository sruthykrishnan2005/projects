from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Service, Testimonial
# Home page view




def home(request):
        services = Service.objects.all()
        testimonials = Testimonial.objects.all()
        return render(request, 'home.html', {'services': services, 'testimonials': testimonials})



# About page view
def about(request):
    return render(request, 'about.html')

# Contact Us page view
def contact(request):
    return render(request, 'contact.html')

