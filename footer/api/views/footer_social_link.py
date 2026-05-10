from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from footer.api.serializers import FooterSocialLinkSerializer
from footer.models import FooterSocialLink


class FooterSocialLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterSocialLink.objects.all()
    serializer_class = FooterSocialLinkSerializer
    permission_classes = [AllowAny]
