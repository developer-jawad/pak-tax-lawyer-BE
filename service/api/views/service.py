from django.core.cache import cache
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

SERVICE_CACHE_KEY = "api:service:list"
SERVICE_CACHE_TTL = 60 * 60


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            cached = cache.get(SERVICE_CACHE_KEY)
        except Exception:
            cached = None
        if cached is not None:
            return Response(cached)

        services = Service.active_objects.all()
        hero_section = ServiceHero.active_objects.first()
        benefits = ServiceBenefit.active_objects.all()
        cta = ServiceCTA.active_objects.filter(is_service_section=False).first()
        statistics = ServiceStatistic.active_objects.all()

        data = {
            "services": ServiceSerializer(services, many=True).data,
            "hero_section": (
                ServiceHeroSerializer(hero_section).data if hero_section else None
            ),
            "benefits": ServiceBenefitSerializer(benefits, many=True).data,
            "cta": ServiceCTASerializer(cta).data if cta else None,
            "statistics": ServiceStatisticSerializer(statistics, many=True).data,
        }
        try:
            cache.set(SERVICE_CACHE_KEY, data, SERVICE_CACHE_TTL)
        except Exception:
            pass
        return Response(data)
