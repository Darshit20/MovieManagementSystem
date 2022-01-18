from django.urls import path
from .views import *

urlpatterns = [
    path('create_playlist/', CreatePlaylist.as_view()),
    path('add_to_playlist/<int:playlist_id>/', addToPlaylist.as_view()),
    path('get_all_playlist_nested/', GetAllPlaylistNested.as_view()),
    path('get_user_playlist/<int:playlist_id>', GetUserPlaylist.as_view()),

]
