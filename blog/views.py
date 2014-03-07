from django.shortcuts import render, render_to_response
from django.utils.datetime_safe import strftime
import pytumblr, time

api_key = "b3ceq6L4SAk28pxX0gpUsXZrcgtQlv82Uakpx6Ki2GIlSn5eNY"
tumblrName = "khanhluc.tumblr.com"
limit = 20

def index(request):

    client = pytumblr.TumblrRestClient(
        consumer_key=api_key,
    )
    posts = client.posts(tumblrName, filter='text', limit=limit)
    data = {"timeline":
                {
                    "headline": "Live, Love, Learn",
                    "type": "default",
                    "text": "The Life of a Photogrammer",
                }
            }

    date = {}

    for post in posts[u'posts']:
        entry = {
            "startDate":strftime("%Y,%m,%d", post[u'timestamp']),
            "headline":"",
            "text":post[u'text']
        }
        if post[u'type'] == u'video':
            entry["asset"] = {
                "media":post[u'permalink_url']
            }


    context = {"title": "Blog", "posts": posts[u'posts'], "blog": True}
    return render(request, 'blog/index.html', context)

def page(request):

    if request.method == 'GET' and request.is_ajax():
        client = pytumblr.TumblrRestClient(consumer_secret=api_key)

        posts = client.posts(tumblrName, filter='text', limit=limit, offset=limit*request.GET['page'])
        context = {"posts": posts}
        render_to_response('blog/posts.html', context)