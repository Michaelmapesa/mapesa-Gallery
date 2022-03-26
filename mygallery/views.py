from turtle import title
from django.shortcuts import render,redirect 
from django.http import HttpResponse, Http404
from .models import Image, Location, Category

# Create your views here.
def index(request):
    images=Image.get_all_images()
    locations=Location.objects.all()
    title= 'My-Gallery'

    return render(request, 'index.html',{'title':title, 'images':images,'locations':locations})

def single

