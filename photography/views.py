from django.shortcuts import render
import flickrapi
import json

api_key = "63cee3b6bc72105b32cbed186ee52655"

def index(request):
    flickr = flickrapi.FlickrAPI(api_key, format='etree')
    sets = flickr.photosets_getList(user_id='49585808@N08')
    children = sets.find('photosets').findall('photoset')

    context = {'photography':True, 'sets': children, 'title': "Photography"}

    return render(request, 'photography/index.html', context)
