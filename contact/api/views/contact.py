from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

CONTACT_CACHE_KEY = "api:contact:page"
CONTACT_CACHE_TTL = 60 * 15

from contact.api.serializers import (
    ContactCTASerializer,
    ContactFormSerializer,
    ContactHeroSerializer,
    ContactInfoSerializer,
    ContactMapSerializer,
    ContactStatisticSerializer,
)
from contact.models import (
    ContactCTA,
    ContactForm,
    ContactHero,
    ContactInfo,
    ContactMap,
    ContactStatistic,
)


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactHero.objects.all()
    serializer_class = ContactHeroSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        cached = cache.get(CONTACT_CACHE_KEY)
        if cached is not None:
            return Response(cached)

        hero = ContactHero.active_objects.first()
        hero_statistics = ContactStatistic.active_objects.all()
        contact_info = ContactInfo.active_objects.all()
        form = ContactForm.active_objects.first()
        map = ContactMap.active_objects.first()
        cta = ContactCTA.active_objects.first()

        data = {
            "hero": {
                "hero": ContactHeroSerializer(hero).data if hero else None,
                "statistics": ContactStatisticSerializer(
                    hero_statistics, many=True
                ).data,
            },
            "contact_info": ContactInfoSerializer(contact_info, many=True).data,
            "form": ContactFormSerializer(form).data if form else None,
            "map": ContactMapSerializer(map).data if map else None,
            "cta": ContactCTASerializer(cta).data if cta else None,
        }
        cache.set(CONTACT_CACHE_KEY, data, CONTACT_CACHE_TTL)
        return Response(data)
