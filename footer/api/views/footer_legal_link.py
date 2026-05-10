from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from footer.api.serializers import FooterLegalLinkSerializer
from footer.models import FooterLegalLink


class FooterLegalLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterLegalLink.objects.all()
    serializer_class = FooterLegalLinkSerializer
    permission_classes = [AllowAny]
