from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from footer.api.serializers import FooterQuickLinkSerializer
from footer.models import FooterQuickLink


class FooterQuickLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterQuickLink.objects.all()
    serializer_class = FooterQuickLinkSerializer
    permission_classes = [AllowAny]
