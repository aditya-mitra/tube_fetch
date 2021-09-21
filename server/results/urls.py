from django.urls import path

from results.views import YTResultsListView, YoutubeAPIKeyView

urlpatterns = [
    path("", YTResultsListView.as_view(), name="list-yt-videos"),
    path("yt-api-key", YoutubeAPIKeyView.as_view(), name="list-add-yt-api-keys"),
]
