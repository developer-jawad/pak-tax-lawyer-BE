from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from contact.api.serializers import ContactInfoSerializer
from contact.models import ContactInfo


class ContactInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [AllowAny]
