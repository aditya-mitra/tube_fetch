from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from results.models import YTResult
from results.serializers import YTResultsSerializer


class YTResultsListView(ListAPIView):
    serializer_class = YTResultsSerializer
    queryset = YTResult.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("title", "description")
    ordering_fields = ("published_date", "title")
