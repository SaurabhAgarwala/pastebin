from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'posts'

urlpatterns = [
    path(r'^$', views.create, name="post_create"),
    path(r'^loggedin_create$', views.login_create, name="post_login_create"),
    path(r'^(?P<url>[\w-]+)/$', views.paste_disp, name="disp"),
    path(r'^loggedin/(?P<url>[\w-]+)/$', views.login_paste_disp, name="login_disp"),
    path(r'^edit/(?P<id>[\w-]+)/$', views.edit, name="edit"),
    path(r'^delete/(?P<id>[\w-]+)/$', views.delete, name="delete"),
]

urlpatterns += staticfiles_urlpatterns()