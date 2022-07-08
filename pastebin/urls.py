from django.contrib import admin
from django.urls import include, path

from posts import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from posts import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^posts/', include('posts.urls')),
    path(r'^accounts/', include('accounts.urls')),
    path(r'^$', views.create, name="home"),
]

urlpatterns += staticfiles_urlpatterns()