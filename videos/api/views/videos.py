from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from videos.models import (
    VideoHero,
    VideoStatistic,
    Video,
    VideoCTA,
)
from videos.api.serializers import (
    VideoHeroSerializer,
    VideoStatisticSerializer,
    VideoSerializer,
    VideoCTASerializer,
)


class VideosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoHero.objects.all()
    serializer_class = VideoHeroSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        hero = VideoHero.active_objects.first()
        hero_statistics = VideoStatistic.active_objects.all()
        videos = Video.active_objects.all()
        cta = VideoCTA.active_objects.first()

        return Response({
            'hero': {
                'hero': VideoHeroSerializer(hero).data if hero else None,
                'statistics': VideoStatisticSerializer(hero_statistics, many=True).data,
            },
            'videos': VideoSerializer(videos, many=True).data,
            'cta': VideoCTASerializer(cta).data if cta else None,
        })
