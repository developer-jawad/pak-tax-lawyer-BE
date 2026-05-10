from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from contact.models import ContactHero
from contact.api.serializers import ContactHeroSerializer


class ContactHeroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactHero.objects.all()
    serializer_class = ContactHeroSerializer
    permission_classes = [AllowAny]
