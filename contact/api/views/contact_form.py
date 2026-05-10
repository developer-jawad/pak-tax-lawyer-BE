from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from contact.api.serializers import ContactFormSerializer
from contact.models import ContactForm


class ContactFormViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [AllowAny]
