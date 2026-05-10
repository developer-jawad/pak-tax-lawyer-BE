from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from videos.models import VideoHero
from videos.api.serializers import VideoHeroSerializer


class VideoHeroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoHero.objects.all()
    serializer_class = VideoHeroSerializer
    permission_classes = [AllowAny]
