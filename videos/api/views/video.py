from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from videos.api.filters import VideoFilter
from videos.api.serializers import VideoSerializer
from videos.models import Video


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.filter(is_active=True, is_deleted=False)
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = VideoFilter
    search_fields = ["title", "description"]
