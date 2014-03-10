__author__ = 'khanh'

from django.conf.urls import patterns, url

from photography import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^gallery/(?P<gallery_id>\d+)/.*$', views.gallery, name='gallery'),
    # ex: /polls/5/
    #url(r'^(?P<page_id>\d+)/$', views.page, name='page'),
    # ex: /polls/5/results/
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)