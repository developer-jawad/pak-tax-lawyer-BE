from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from about.api.serializers import AboutValueSerializer
from about.models import AboutValue


class AboutValueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutValue.objects.all()
    serializer_class = AboutValueSerializer
    permission_classes = [AllowAny]
