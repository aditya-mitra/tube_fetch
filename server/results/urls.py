from django.urls import path

from results.views import YTResultsListView

urlpatterns = [path("", YTResultsListView.as_view(), name="list-yt-videos")]
