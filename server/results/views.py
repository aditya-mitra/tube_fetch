from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from results.models import YTResult
from results.serializers import YTResultsSerializer


class YTResultsListView(ListAPIView):
    serializer_class = YTResultsSerializer
    queryset = YTResult.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title','description']