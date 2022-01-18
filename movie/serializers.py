from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


class CreatePlaylistSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Playlist
        fields = ['id', 'user_id', 'name', 'type']


class addToPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist_data
        fields = ['id', 'playlist_id', 'imdb_id']

class GetAllPlaylistNestedSerializer(serializers.ModelSerializer):
    playlists_data = addToPlaylistSerializer(many=True, read_only=False)
    class Meta:
        model = Playlist
        fields = ['id', 'user_id', 'name', 'type','playlists_data']

class GetUserPlaylistSerializer(serializers.ModelSerializer):
    playlists_data = addToPlaylistSerializer(many=True, read_only=False)
    class Meta:
        model = Playlist
        fields = ['id', 'user_id', 'name', 'type','playlists_data']

        