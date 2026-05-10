from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from service.api.serializers import (
    ServiceCTASerializer,
    ServiceSectionSerializer,
    ServiceSerializer,
)
from service.models import Service, ServiceCTA, ServiceSection


class ServiceSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceSection.objects.all()
    serializer_class = ServiceSectionSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        service_section = ServiceSection.active_objects.first()
        services = Service.active_objects.all()
        cta = ServiceCTA.active_objects.filter(is_service_section=True).first()

        return Response(
            {
                "service_section": (
                    ServiceSectionSerializer(service_section).data
                    if service_section
                    else None
                ),
                "services": ServiceSerializer(services, many=True).data,
                "cta": ServiceCTASerializer(cta).data if cta else None,
            }
        )
