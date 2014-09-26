import pytumblr
import datetime

api_key = "b3ceq6L4SAk28pxX0gpUsXZrcgtQlv82Uakpx6Ki2GIlSn5eNY"
tumblrName = "khanhluc.tumblr.com"
limit = 10

def getPost(post_id=0):

    client = pytumblr.TumblrRestClient(
        consumer_key=api_key,
    )
    post = client.posts(tumblrName, id=post_id)
    entry = {}
    if post:
        post = post[u'posts'][0]
        entry["date"] = post[u'date']
        entry["timestamp"] = datetime.datetime.fromtimestamp(post[u'timestamp'])
        entry["slug"] = post[u'slug']
        entry["reblog_key"] = post[u'reblog_key']
        entry["short_url"] = post[u'short_url']
        entry["type"] = post[u'type']

        if post[u'type'] == u'video':
            player = post[u'player']
            entry["content"] = player[2]['embed_code']
    return entry

def getPosts(page=0):

    client = pytumblr.TumblrRestClient(
        consumer_key=api_key,
    )
    posts = client.posts(tumblrName, limit=limit, offset=(page-1)*limit)

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
            entry["id"] = post[u'id']

            if u'thumbnail_url' in post:
                entry["content"] = "<img class=\"modal-btn\" data-toggle=\"modal\" data-target=\"#blog-modal\" src=\""+post[u'thumbnail_url']+"\">"
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
            content = ""
            for photo in post[u'photos']:
                content = content+"<img class=\"modal-btn blog-photo\" data-toggle=\"modal\" data-target=\"#blog-modal\" src=\""+photo[u'alt_sizes'][0][u'url']+"\"/>"
            entry["content"] = content;
        elif post[u'type'] == u'link':
            entry["title"] = post[u'title']
            entry["content"] = post[u'description']
            entry["url"] = post[u'url']

        formattedPosts.append(entry)

    return formattedPosts