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
    posts = client.posts(tumblrName, limit=limit)

    formattedPosts = []

    for post in posts[u'posts']:
        entry = {}

        entry["date"] = post[u'date']
        entry["timestamp"] = datetime.datetime.fromtimestamp(post[u'timestamp'])
        entry["slug"] = post[u'slug']
        entry["reblog_key"] = post[u'reblog_key']
        entry["short_url"] = post[u'short_url']
        entry["type"] = post[u'type']

        if post[u'type'] == u'video':
            entry["caption"] = post[u'caption']
            player = post[u'player']
            entry["content"] = player[2]['embed_code']
            entry["icon"] = "glyphicon glyphicon-film"

        elif post[u'type'] == u'text':
            entry["title"] = post[u'title']
            entry["content"] = post[u'body']
        elif post[u'type'] == u'quote':
            entry["content"] = "\""+post[u'text']+"\""
            entry["source"] = post[u'source']
        elif post[u'type'] == u'audio':
            entry["title"] = post[u'track_name']
            entry["content"] = post[u'embed']
        elif post[u'type'] == u'photo':
            entry["caption"] = post[u'caption']
            entry["content"] = "<img src=\""+post[u'photos'][0][u'alt_sizes'][1][u'url']+"\"/>"
        elif post[u'type'] == u'link':
            entry["title"] = post[u'title']
            entry["content"] = post[u'description']
            entry["url"] = post[u'url']

        formattedPosts.append(entry)

    context = {"title": "Blog", "posts": formattedPosts, "blog": True}
    return render(request, 'blog/index.html', context)

def page(request):

    if request.method == 'GET' and request.is_ajax():
        client = pytumblr.TumblrRestClient(consumer_secret=api_key)

        posts = client.posts(tumblrName, filter='text', limit=limit, offset=limit*request.GET['page'])
        context = {"posts": posts}
        render_to_response('blog/posts.html', context)