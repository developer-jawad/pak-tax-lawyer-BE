from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from about.models import AboutValue
from about.api.serializers import AboutValueSerializer


class AboutValueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutValue.objects.all()
    serializer_class = AboutValueSerializer
    permission_classes = [AllowAny]
