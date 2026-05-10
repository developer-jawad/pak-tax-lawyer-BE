from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from about.api.serializers import AboutStatisticSectionSerializer
from about.models import AboutStatisticSection


class AboutStatisticSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutStatisticSection.objects.all()
    serializer_class = AboutStatisticSectionSerializer
    permission_classes = [AllowAny]
