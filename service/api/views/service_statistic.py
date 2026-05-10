from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from service.models import ServiceStatistic
from service.api.serializers import ServiceStatisticSerializer


class ServiceStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceStatistic.objects.all()
    serializer_class = ServiceStatisticSerializer
    permission_classes = [AllowAny]
