from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from contact.models import ContactMap
from contact.api.serializers import ContactMapSerializer


class ContactMapViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactMap.objects.all()
    serializer_class = ContactMapSerializer
    permission_classes = [AllowAny]
