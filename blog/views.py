from django.shortcuts import render, render_to_response
import datetime
import json
import pytumblr


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

    date = []

    for post in posts[u'posts']:
        entry = {
            "startDate": (datetime.datetime.fromtimestamp(post[u'timestamp'])).strftime("%Y,%m,%d"),
            "headline": "",
        }

        if post[u'type'] == u'video':
            entry["text"] = post[u'caption']

            if u'permalink_url' in post:
                entry["asset"] = {
                    "media": post[u'permalink_url']
                }
            else:
                player = post[u'player']
                entry["text"] = player[0]['embed_code']

        elif post[u'type'] == u'text':
            entry["headline"] = post[u'title']
            entry["text"] = post[u'body']
        elif post[u'type'] == u'quote':
            entry["text"] = "\""+post[u'text']+"\""
            entry["headline"] = post[u'source']
        elif post[u'type'] == u'audio':
            entry["headline"] = post[u'track_name']
            entry["asset"] = {
                "media": post[u'embed'],
            }
        elif post[u'type'] == u'photo':
            entry["text"] = post[u'caption']
            entry["asset"] = {
                "media": post[u'photos'][0][u'alt_sizes'][1][u'url']
            }
        elif post[u'type'] == u'link':
            entry["headline"] = post[u'title']
            entry["text"] = post[u'description']
            entry["asset"] = {
                "media": post[u'url']
            }

        date.append(entry)

    data["timeline"]["date"] = date

    timeline = json.dumps(data)

    context = {"title": "Blog", "timeline": timeline, "blog": True}
    return render(request, 'blog/index.html', context)

def page(request):

    if request.method == 'GET' and request.is_ajax():
        client = pytumblr.TumblrRestClient(consumer_secret=api_key)

        posts = client.posts(tumblrName, filter='text', limit=limit, offset=limit*request.GET['page'])
        context = {"posts": posts}
        render_to_response('blog/posts.html', context)