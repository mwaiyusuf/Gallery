from django.shortcuts import render
from django.http  import HttpResponse  #returning response to user
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')