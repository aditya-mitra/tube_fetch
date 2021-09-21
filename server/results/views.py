from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, ListCreateAPIView

from results.models import YTResult, YoutubeAPIKey
from results.serializers import YTResultsSerializer, YoutubeAPIKeySerializer


class YTResultsListView(ListAPIView):
    serializer_class = YTResultsSerializer
    queryset = YTResult.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ("title", "description")
    ordering_fields = ("published_date", "title")


class YoutubeAPIKeyView(ListCreateAPIView):
    serializer_class = YoutubeAPIKeySerializer
    queryset = YoutubeAPIKey.objects.all()
