from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from footer.api.serializers import FooterServiceLinkSerializer
from footer.models import FooterServiceLink


class FooterServiceLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterServiceLink.objects.all()
    serializer_class = FooterServiceLinkSerializer
    permission_classes = [AllowAny]
