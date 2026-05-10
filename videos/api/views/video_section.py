from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from videos.models import VideoSection
from videos.api.serializers import VideoSectionSerializer


class VideoSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoSection.objects.all()
    serializer_class = VideoSectionSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        video_section = VideoSection.active_objects.first()
        videos = Video.active_objects.all()
        cta = VideoCTA.active_objects.first()

        return Response({
            'section': VideoSectionSerializer(video_section).data if video_section else None,
            'videos': VideoSerializer(videos, many=True).data,
            'cta': VideoCTASerializer(cta).data if cta else None,
        })
