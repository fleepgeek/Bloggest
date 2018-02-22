from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from blog import views

urlpatterns = [
    url(r'^post/cat/(?P<pk>[\d]+)/$', views.PostCategory.as_view(), name='post_by_category'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    url(r'^dashboard/$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^post/(?P<pk>[\d]+)/delete/$', views.PostDelete.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>[\d]+)/update/$', views.PostUpdate.as_view(), name='post_update'),
    url(r'^post/add/$', views.PostCreate.as_view(), name='post_add'),
    url(r'^post/(?P<pk>[\d]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^$', views.Home.as_view(), name='home'),
]
