from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect #returning response to user
from .models import *

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def home(request):
  images = image.objects.all()
  location = Location.objects.all()
  category = Categories.objects.all()

  if 'location'  in request.GET and request.GET['location']:
    name = request.GET.get('location')
    images = Image.view_location(name)

  elif 'category' in request.GET and request.GET['category']:
    name = request.GET.get('categories')
    images = Image.view_category(name)
    return render(request, 'all-images.html', {"name":name,"images":images,"name":name})

  return render(request,"all-images.html",{"images":images,"category":category,"location":location})

    


