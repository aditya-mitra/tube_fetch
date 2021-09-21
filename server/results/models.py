from django.db import models


class YTResult(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    thumbnail_url = models.URLField()
    description = models.TextField()
    published_date = models.DateTimeField()
