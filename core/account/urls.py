from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',
    url(r'^$', views.all_users, name='all_users'),
    url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
)