__author__ = 'khanh'
from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<page_id>\d+)$', views.page, name='page'),
    url(r'^(?P<post_id>\d+)/post/$', views.post, name='post')
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)