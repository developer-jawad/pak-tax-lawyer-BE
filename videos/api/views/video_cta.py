from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from videos.api.serializers import VideoCTASerializer
from videos.models import VideoCTA


class VideoCTAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoCTA.objects.all()
    serializer_class = VideoCTASerializer
    permission_classes = [AllowAny]
