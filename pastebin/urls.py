from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import include, path

from posts import views
>>>>>>> dfb626da0de55b300e62c00cefa80145541efae3
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('posts.urls')),
=======
    path(r'^admin/', admin.site.urls),
    path(r'^posts/', include('posts.urls')),
    path(r'^accounts/', include('accounts.urls')),
    path(r'^$', views.create, name="home"),
>>>>>>> dfb626da0de55b300e62c00cefa80145541efae3
]

urlpatterns += staticfiles_urlpatterns()