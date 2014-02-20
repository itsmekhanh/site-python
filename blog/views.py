from django.shortcuts import render
import pytumblr

def index(request):
    context = {"title": "Blog"}
    return render(request, 'blog/index.html', context)