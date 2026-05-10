from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from contact.api.serializers import ContactCTASerializer
from contact.models import ContactCTA


class ContactCTAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactCTA.objects.all()
    serializer_class = ContactCTASerializer
    permission_classes = [AllowAny]
