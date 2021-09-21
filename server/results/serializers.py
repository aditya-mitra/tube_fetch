from rest_framework.serializers import ModelSerializer

from results.models import YTResult


class YTResultsSerializer(ModelSerializer):
    class Meta:
        model = YTResult
        fields = (
            "id",
            "video_id",
            "title",
            "thumbnail_url",
            "description",
            "published_date",
        )
