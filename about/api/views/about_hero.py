from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from about.models import AboutHero
from about.api.serializers import AboutHeroSerializer


class AboutHeroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutHero.objects.all()
    serializer_class = AboutHeroSerializer
    permission_classes = [AllowAny]
