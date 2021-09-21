from rest_framework.generics import ListAPIView

from results.models import YTResult
from results.serializers import YTResultsSerializer


class YTResultsListView(ListAPIView):
    serializer_class = YTResultsSerializer
    queryset = YTResult.objects.all()
