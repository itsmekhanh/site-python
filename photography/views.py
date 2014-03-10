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


def gallery(request, gallery_id):

    flickr = flickrapi.FlickrAPI(api_key, format='etree')
    try:
        set = flickr.photosets_getPhotos(photoset_id=gallery_id)
        context = {"set": set}
        return render(request, 'photography/gallery.html', context)
    except flickrapi.FlickrError:
        return render(request, 'main/index.html')



