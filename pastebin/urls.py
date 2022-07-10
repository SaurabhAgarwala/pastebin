from django.contrib import admin
from django.urls import path, include
from posts import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.create, name="home"),
]

urlpatterns += staticfiles_urlpatterns()