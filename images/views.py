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


