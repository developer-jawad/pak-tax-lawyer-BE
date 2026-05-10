from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from service.api.serializers import ServiceCTASerializer
from service.models import ServiceCTA


class ServiceCTAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceCTA.objects.all()
    serializer_class = ServiceCTASerializer
    permission_classes = [AllowAny]
