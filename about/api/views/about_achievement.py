from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from about.models import AboutAchievement
from about.api.serializers import AboutAchievementSerializer


class AboutAchievementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutAchievement.objects.all()
    serializer_class = AboutAchievementSerializer
    permission_classes = [AllowAny]
