from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from about.models import AboutStatistic
from about.api.serializers import AboutStatisticSerializer


class AboutStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutStatistic.objects.all()
    serializer_class = AboutStatisticSerializer
    permission_classes = [AllowAny]
