from django.conf.urls import url
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^dashboard/$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^post/(?P<pk>[\d]+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>[\d]+)/update/$', views.PostUpdate.as_view(), name='post_update'),
    url(r'^post/add/$', views.PostCreate.as_view(), name='post_add'),
    url(r'^post/(?P<pk>[\d]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^$', views.Home.as_view(), name='home'),
]
