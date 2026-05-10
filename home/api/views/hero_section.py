from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from home.api.serializers import HeroSectionSerializer
from home.models import HeroSection


class HeroSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HeroSection.objects.filter(is_active=True, is_deleted=False)
    serializer_class = HeroSectionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-created_at")
