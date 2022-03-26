from email.mime import image
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

def single(request,category_name,image_id):
    title='Image'
    locations=Location.objects.all()
    image_category=Image.objects.filter(image_category__name = category_name)
    try:
        image = Image.objects.get(id=image_id)
    except ValueError:
        raise Http404()
        return render(request,"single.html",{'title':title,"image":image,"locations":locations,"image_category":image_category})


