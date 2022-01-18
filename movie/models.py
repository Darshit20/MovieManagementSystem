from django.db import models

# Create your models here.

from django.conf import settings


class Playlist(models.Model):
    playlist_type = (
        ("PUBLIC", "PUBLIC"),
        ("PRIVATE", "PRIVATE"),
    )
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="playlists")
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256, choices=playlist_type)
    def __str__(self):
        return self.name


class Playlist_data(models.Model):
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="playlists_data")
    imdb_id = models.CharField(max_length=256)
    
    class Meta:
        unique_together =[['playlist_id', 'imdb_id']]

    def __str__(self):
        return self.playlist_id + self.imdb_id

