<<<<<<< HEAD
# from django.conf.urls import url
from django.urls import re_path
=======
from django.urls import path
>>>>>>> dfb626da0de55b300e62c00cefa80145541efae3
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# app_name = 'posts'

urlpatterns = [
<<<<<<< HEAD
    re_path(r'^$', views.create, name="post_create"),
    re_path(r'^loggedin_create$', views.login_create, name="post_login_create"),
    re_path(r'^(?P<url>[\w-]+)/$', views.paste_disp, name="disp"),
    re_path(r'^loggedin/(?P<url>[\w-]+)/$', views.login_paste_disp, name="login_disp"),
    re_path(r'^edit/(?P<id>[\w-]+)/$', views.edit, name="edit"),
    re_path(r'^delete/(?P<id>[\w-]+)/$', views.delete, name="delete"),
=======
    path(r'^$', views.create, name="post_create"),
    path(r'^loggedin_create$', views.login_create, name="post_login_create"),
    path(r'^(?P<url>[\w-]+)/$', views.paste_disp, name="disp"),
    path(r'^loggedin/(?P<url>[\w-]+)/$', views.login_paste_disp, name="login_disp"),
    path(r'^edit/(?P<id>[\w-]+)/$', views.edit, name="edit"),
    path(r'^delete/(?P<id>[\w-]+)/$', views.delete, name="delete"),
>>>>>>> dfb626da0de55b300e62c00cefa80145541efae3
]

urlpatterns += staticfiles_urlpatterns()