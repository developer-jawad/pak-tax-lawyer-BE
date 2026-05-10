from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from service.models import ServiceSection
from service.api.serializers import ServiceSectionSerializer


class ServiceSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceSection.objects.all()
    serializer_class = ServiceSectionSerializer
    permission_classes = [AllowAny]
