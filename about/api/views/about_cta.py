from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from about.models import AboutCTA
from about.api.serializers import AboutCTASerializer


class AboutCTAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutCTA.objects.all()
    serializer_class = AboutCTASerializer
    permission_classes = [AllowAny]
