from django.shortcuts import render
import flickrapi

api_key = "63cee3b6bc72105b32cbed186ee52655"

def index(request):
    flickr = flickrapi.FlickrAPI(api_key, format='etree')
    sets = flickr.photosets_getList(user_id='49585808@N08', page=1, per_page=3)
    context = {"title": "Home", "featuredGalleries": sets._children[0]._children}
    return render(request, 'main/index.html', context)