from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from videos.api.serializers import VideoStatisticSerializer
from videos.models import VideoStatistic


class VideoStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoStatistic.objects.all()
    serializer_class = VideoStatisticSerializer
    permission_classes = [AllowAny]
