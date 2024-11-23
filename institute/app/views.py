from django.shortcuts import render
from .models import Course

def home_view(request):
    nav_links = Course.objects.filter()  # Fetch active links
    return render(request, 'home.html', {'nav_links': nav_links})

def about_view(request):
    nav_links = Course.objects.filter()
    return render(request, 'about.html', {'nav_links': nav_links})

def contact_view(request):
    nav_links = Course.objects.filter()
    return render(request, 'contact.html', {'nav_links': nav_links})
  