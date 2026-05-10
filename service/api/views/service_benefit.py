from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from service.models import ServiceBenefit
from service.api.serializers import ServiceBenefitSerializer


class ServiceBenefitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceBenefit.objects.all()
    serializer_class = ServiceBenefitSerializer
    permission_classes = [AllowAny]
