from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from service.api.serializers import (
    ServiceBenefitSerializer,
    ServiceCTASerializer,
    ServiceHeroSerializer,
    ServiceSerializer,
    ServiceStatisticSerializer,
)
from service.models import (
    Service,
    ServiceBenefit,
    ServiceCTA,
    ServiceHero,
    ServiceStatistic,
)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        services = Service.active_objects.all()
        hero_section = ServiceHero.active_objects.first()
        benefits = ServiceBenefit.active_objects.all()
        cta = ServiceCTA.active_objects.filter(is_service_section=False).first()
        statistics = ServiceStatistic.active_objects.all()

        return Response(
            {
                "services": ServiceSerializer(services, many=True).data,
                "hero_section": (
                    ServiceHeroSerializer(hero_section).data if hero_section else None
                ),
                "benefits": ServiceBenefitSerializer(benefits, many=True).data,
                "cta": ServiceCTASerializer(cta).data if cta else None,
                "statistics": ServiceStatisticSerializer(statistics, many=True).data,
            }
        )
