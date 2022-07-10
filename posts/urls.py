# from django.conf.urls import url
from django.urls import re_path
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# app_name = 'posts'

urlpatterns = [
    re_path(r'^$', views.create, name="post_create"),
    re_path(r'^loggedin_create$', views.login_create, name="post_login_create"),
    re_path(r'^(?P<url>[\w-]+)/$', views.paste_disp, name="disp"),
    re_path(r'^loggedin/(?P<url>[\w-]+)/$', views.login_paste_disp, name="login_disp"),
    re_path(r'^edit/(?P<id>[\w-]+)/$', views.edit, name="edit"),
    re_path(r'^delete/(?P<id>[\w-]+)/$', views.delete, name="delete"),
]

urlpatterns += staticfiles_urlpatterns()