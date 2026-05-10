from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from contact.models import ContactInfo
from contact.api.serializers import ContactInfoSerializer


class ContactInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [AllowAny]
