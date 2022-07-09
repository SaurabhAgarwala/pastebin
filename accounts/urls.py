from django.urls import path
<<<<<<< HEAD
=======

>>>>>>> dfb626da0de55b300e62c00cefa80145541efae3
from . import views


urlpatterns = [
<<<<<<< HEAD
   path('signup/', views.signup_view, name="signup"),
   path('login/', views.login_view, name="login"),
   path('logout/', views.logout_view, name="logout"),
=======
   path(r'^signup/$', views.signup_view, name="signup"),
   path(r'^login/$', views.login_view, name="login"),
   path(r'^logout/$', views.logout_view, name="logout"),
>>>>>>> dfb626da0de55b300e62c00cefa80145541efae3
]   