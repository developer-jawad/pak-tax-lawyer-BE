from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from footer.api.serializers import FooterBrandSerializer
from footer.models import FooterBrand


class FooterBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterBrand.objects.all()
    serializer_class = FooterBrandSerializer
    permission_classes = [AllowAny]
