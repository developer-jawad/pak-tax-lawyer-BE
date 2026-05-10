from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from videos.api.serializers import VideoHeroSerializer
from videos.models import VideoHero


class VideoHeroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoHero.objects.all()
    serializer_class = VideoHeroSerializer
    permission_classes = [AllowAny]
