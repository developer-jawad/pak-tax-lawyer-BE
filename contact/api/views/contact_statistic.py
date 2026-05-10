from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from contact.api.serializers import ContactStatisticSerializer
from contact.models import ContactStatistic


class ContactStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactStatistic.objects.all()
    serializer_class = ContactStatisticSerializer
    permission_classes = [AllowAny]
