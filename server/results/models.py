from django.db import models


class YTResult(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200, db_index=True)
    thumbnail_url = models.URLField()
    description = models.TextField()
    published_date = models.DateTimeField(db_index=True)


class YoutubeAPIKey(models.Model):
    api_key = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=100, blank=True)
    available = models.DateField(auto_now_add=True)
