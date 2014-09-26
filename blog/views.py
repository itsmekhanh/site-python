from django.shortcuts import render, render_to_response, redirect
from utils import *

def index(request):

    formattedPosts = getPosts()
    context = {"title": "Blog", "posts": formattedPosts, "blog": True}
    return render(request, 'blog/index.html', context)

def page(request, page_id):

    if request.method == 'GET' and request.is_ajax():

        page = int(page_id)
        posts = getPosts(page)
        context = {"posts": posts}
        return render_to_response('blog/posts.html', context)
    else:
        return redirect('/')

def post(request, post_id):
    if request.method == "GET" and request.is_ajax():
        id = int(post_id)
        post = getPost(id)
        context = {"post":post}
        return render_to_response('blog/post.html', context)