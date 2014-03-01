from django.shortcuts import render, render_to_response
import pytumblr

api_key = "b3ceq6L4SAk28pxX0gpUsXZrcgtQlv82Uakpx6Ki2GIlSn5eNY"
tumblrName = "khanhluc.tumblr.com"
limit = 20

def index(request):

    client = pytumblr.TumblrRestClient(
        consumer_key=api_key,
    )
    posts = client.posts(tumblrName, filter='text', limit=limit)

    context = {"title": "Blog", "posts": posts[u'posts'], "blog": True}
    return render(request, 'blog/index.html', context)

def page(request, page_id):

    if request.method == 'GET' and request.is_ajax():
        client = pytumblr.TumblrRestClient(consumer_secret=api_key)

        posts = client.posts(tumblrName, filter='text', limit=limit, offset=limit*request.GET['page'])
        context = {"posts": posts}
        render_to_response('blog/posts.html', context)