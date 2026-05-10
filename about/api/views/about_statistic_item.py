from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from about.api.serializers import AboutStatisticItemSerializer
from about.models import AboutStatisticItem


class AboutStatisticItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutStatisticItem.objects.all()
    serializer_class = AboutStatisticItemSerializer
    permission_classes = [AllowAny]
