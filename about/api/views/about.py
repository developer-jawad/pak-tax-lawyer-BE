from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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
        hero = AboutHero.active_objects.first()
        hero_statistics = AboutStatistic.active_objects.all()
        who_we_are = WhoWeAre.active_objects.first()
        statistic_section = AboutStatisticSection.active_objects.first()
        statistic_items = AboutStatisticItem.active_objects.all()
        values = AboutValue.active_objects.all()
        achievements = AboutAchievement.active_objects.all()
        cta = AboutCTA.active_objects.first()

        return Response(
            {
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
        )
