from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from service.api.serializers import ServiceHeroSerializer
from service.models import ServiceHero


class ServiceHeroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceHero.objects.all()
    serializer_class = ServiceHeroSerializer
    permission_classes = [AllowAny]
