from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name=""),
    # path('home', views.home, name="home-page"),
    path('playlist', views.playlist, name="playlist-page"),
    path('signup', views.signup),
    path('signin', views.signin),
]
