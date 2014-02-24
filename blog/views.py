from django.shortcuts import render
import pytumblr

api_key = "b3ceq6L4SAk28pxX0gpUsXZrcgtQlv82Uakpx6Ki2GIlSn5eNY";

def index(request):
    client = pytumblr.TumblrRestClient(
        consumer_key=api_key,
    )

    posts = client.posts("khanhluc.tumblr.com", filter='text')

    context = {"title": "Blog", "posts": posts[u'posts'], "blog": True}
    return render(request, 'blog/index.html', context)

