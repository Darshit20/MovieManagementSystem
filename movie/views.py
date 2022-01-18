from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class CreatePlaylist(generics.ListCreateAPIView):
    serializer_class = CreatePlaylistSerializer
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        user = self.request.user
        return user.playlists.all()

class addToPlaylist(generics.ListCreateAPIView):
    serializer_class = addToPlaylistSerializer

    def get_queryset(self):
        user = self.request.user
        playlist_id = self.kwargs.get('playlist_id')
        return Playlist_data.objects.filter(playlist_id=playlist_id, playlist_id__user_id=user)
        # return Playlist.playlists_data.objects.filter(playlist_id=playlist_id)

class GetAllPlaylistNested(generics.ListAPIView):
    serializer_class = GetAllPlaylistNestedSerializer

    def get_queryset( self ):
        user = self.request.user
        return Playlist.objects.filter(user_id=user)

class GetUserPlaylist(generics.ListAPIView):
    serializer_class = GetUserPlaylistSerializer

    def get_queryset(self):
        playlist_id = self.kwargs.get('playlist_id')
        user = self.request.user
        
        obj = Playlist.objects.filter(id=playlist_id)

        if obj[0].user_id == user:
            return obj
        elif obj[0].type == "PUBLIC":
            return obj
        else:
            return {}

        