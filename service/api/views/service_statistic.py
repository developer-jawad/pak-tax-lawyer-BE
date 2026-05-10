from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from service.api.serializers import ServiceStatisticSerializer
from service.models import ServiceStatistic


class ServiceStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceStatistic.objects.all()
    serializer_class = ServiceStatisticSerializer
    permission_classes = [AllowAny]
