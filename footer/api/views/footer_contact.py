from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from footer.models import FooterContact
from footer.api.serializers import FooterContactSerializer


class FooterContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterContact.objects.all()
    serializer_class = FooterContactSerializer
    permission_classes = [AllowAny]
