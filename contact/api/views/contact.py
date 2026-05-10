from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from contact.models import (
    ContactHero,
    ContactStatistic,
    ContactInfo,
    ContactForm,
    ContactMap,
    ContactCTA,
)
from contact.api.serializers import (
    ContactHeroSerializer,
    ContactStatisticSerializer,
    ContactInfoSerializer,
    ContactFormSerializer,
    ContactMapSerializer,
    ContactCTASerializer,
)


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactHero.objects.all()
    serializer_class = ContactHeroSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        hero = ContactHero.active_objects.first()
        hero_statistics = ContactStatistic.active_objects.all()
        contact_info = ContactInfo.active_objects.all()
        form = ContactForm.active_objects.first()
        map = ContactMap.active_objects.first()
        cta = ContactCTA.active_objects.first()

        return Response({
            'hero': {
                'hero': ContactHeroSerializer(hero).data if hero else None,
                'statistics': ContactStatisticSerializer(hero_statistics, many=True).data,
            },
            'contact_info': ContactInfoSerializer(contact_info, many=True).data,
            'form': ContactFormSerializer(form).data if form else None,
            'map': ContactMapSerializer(map).data if map else None,
            'cta': ContactCTASerializer(cta).data if cta else None,
        })
