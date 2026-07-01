from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

ABOUT_CACHE_KEY = "api:about:page"
ABOUT_CACHE_TTL = 60 * 60

from about.api.serializers import (
    AboutAchievementSerializer,
    AboutCTASerializer,
    AboutHeroSerializer,
    AboutStatisticItemSerializer,
    AboutStatisticSectionSerializer,
    AboutStatisticSerializer,
    AboutValueSerializer,
    WhoWeAreSerializer,
)
from about.models import (
    AboutAchievement,
    AboutCTA,
    AboutHero,
    AboutStatistic,
    AboutStatisticItem,
    AboutStatisticSection,
    AboutValue,
    WhoWeAre,
)


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutHero.objects.all()
    serializer_class = AboutHeroSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            cached = cache.get(ABOUT_CACHE_KEY)
        except Exception:
            cached = None
        if cached is not None:
            return Response(cached)

        hero = AboutHero.active_objects.first()
        hero_statistics = AboutStatistic.active_objects.all()
        who_we_are = WhoWeAre.active_objects.first()
        statistic_section = AboutStatisticSection.active_objects.first()
        statistic_items = AboutStatisticItem.active_objects.all()
        values = AboutValue.active_objects.all()
        achievements = AboutAchievement.active_objects.all()
        cta = AboutCTA.active_objects.first()

        data = {
            "hero": {
                "hero": AboutHeroSerializer(hero).data if hero else None,
                "statistics": AboutStatisticSerializer(
                    hero_statistics, many=True
                ).data,
            },
            "who_we_are": (
                WhoWeAreSerializer(who_we_are).data if who_we_are else None
            ),
            "statistics": {
                "section": (
                    AboutStatisticSectionSerializer(statistic_section).data
                    if statistic_section
                    else None
                ),
                "items": AboutStatisticItemSerializer(
                    statistic_items, many=True
                ).data,
            },
            "values": AboutValueSerializer(values, many=True).data,
            "achievements": AboutAchievementSerializer(
                achievements, many=True
            ).data,
            "cta": AboutCTASerializer(cta).data if cta else None,
        }
        try:
            cache.set(ABOUT_CACHE_KEY, data, ABOUT_CACHE_TTL)
        except Exception:
            pass
        return Response(data)
