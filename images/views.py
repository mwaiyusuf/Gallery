from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect #returning response to user
from .models import Image,Categories,Location

# Create your views here.


def home(request):
  images = Image.objects.all()
  location = Location.objects.all()
  category = Categories.objects.all()

  if 'location'  in request.GET and request.GET['location']:
    name = request.GET.get('location')
    images = Image.view_location(name)

  elif 'category' in request.GET and request.GET['category']:
    name = request.GET.get('categories')
    images = Image.view_category(name)
    # return render(request, 'base-images.html', {"name":name,"images":images,"name":name})
  return render(request,"base/base-images.html",{"images":images,"category":category,"location":location})


def search_results(request):

    if 'categories' in request.GET and request.GET['categories']:
        search_images = request.GET.get("categories")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})

def get_image_by_id(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})


