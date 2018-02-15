from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^post/new/$', views.PostCreate.as_view(), name='post_new'),
    url(r'^post/(?P<pk>[\d]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^$', views.Home.as_view(), name='home'),
]
