from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from footer.models import FooterBrand
from footer.api.serializers import FooterBrandSerializer


class FooterBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterBrand.objects.all()
    serializer_class = FooterBrandSerializer
    permission_classes = [AllowAny]
