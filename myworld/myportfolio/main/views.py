from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Experience
from .models import Project

def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def projects(request):
    return render(request, "projects.html")
def contact(request):
    return render(request, "contact.html")

# main/views.py


def about(request):
    experiences = Experience.objects.all()
    return render(request, 'about.html', {'experiences': experiences})
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
# Create your views here.
