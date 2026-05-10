from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from footer.api.serializers import FooterBottomSectionSerializer
from footer.models import FooterBottomSection


class FooterBottomSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterBottomSection.objects.all()
    serializer_class = FooterBottomSectionSerializer
    permission_classes = [AllowAny]
